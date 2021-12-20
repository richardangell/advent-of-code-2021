from collections import Counter
import sys

sys.path.append("..")
import helpers  # noqa


def load_input(file: str) -> list[list[str]]:
    """Load the input file."""

    return helpers.load_input_split(file, remove_lines_breaks=True, split_string="-")


def process_input(input: list[list[str]]) -> dict:
    """Convert the input data structure (lists of pairs of caves that are connected)
    into a dict where each key is a cave and the corresponding value is a list of
    all the caves it is contected to.
    """

    input_processed = {}

    cave_pairs = []

    for cave_pair in input:

        cave_pairs.extend(cave_pair)

    unique_caves = set(cave_pairs)

    for cave in unique_caves:

        connected_caves = []

        for cave_pair in input:

            # copy the list, remove the cave of interest and append the other cave
            if cave in cave_pair:

                cave_pair_copy = cave_pair[:]

                cave_pair_copy.remove(cave)

                connected_caves.append(cave_pair_copy[0])

            # remove connections back to start as we do not want to travel back that way
            if "START" in connected_caves:

                connected_caves.remove("START")

        input_processed[cave] = connected_caves

    return input_processed


def find_paths_not_visiting_small_caves_twice(input: dict) -> list[list[str]]:
    """Find all the unique paths that do not visit small caves twice."""

    results = traverse_caves_recursive("START", input, ["START"])

    return results


def traverse_caves_recursive(cave: str, cave_system: dict, current_path: list[str]):
    """Recursively traverse through all paths in the cave."""

    if cave != "START":

        # build the current path traversed
        current_path = current_path[:]
        current_path.append(cave)

    if cave == "END":

        return current_path

    previous_cave_counts = Counter(current_path)

    small_caves_previously_visited = [
        cave
        for cave in previous_cave_counts.keys()
        if cave.islower() and previous_cave_counts[cave] > 0
    ]

    potential_next_caves = [
        cave_
        for cave_ in cave_system[cave]
        if cave_ not in small_caves_previously_visited
    ]

    if len(potential_next_caves) > 0:

        return [
            traverse_caves_recursive(next_cave, cave_system, current_path)
            for next_cave in potential_next_caves
        ]


def unnest_paths(paths: list) -> list:
    """Unnest a nested list of paths. Also removes paths that consist
    entirely of None values.
    """

    def unnest_recursive(list_: list):
        """Recursive checking if a list contains no list elements."""

        if type(list_) is list:

            if all([type(sub_l) is not list for sub_l in list_]):

                # remove lists comprising of just None values
                if not all([sub_l is None for sub_l in list_]):

                    unnested_list.append(list_)

            else:

                for sub_l in list_:

                    unnest_recursive(sub_l)

    unnested_list: list = []

    unnest_recursive(paths)

    return unnested_list


def count_paths_not_visiting_small_caves_twice(input: list[list[str]]) -> int:
    """Find the number of paths that do not visit small caves twice."""

    input_processed = process_input(input)

    nested_paths = find_paths_not_visiting_small_caves_twice(input_processed)

    paths = unnest_paths(nested_paths)

    check_paths(paths)

    return len(paths)


def check_paths(paths_list: list[list[str]]) -> None:
    """Perform checks on the paths that have been returned from
    find_paths_not_visiting_small_caves_twice.
    """

    if not all([type(p) is list for p in paths_list]):

        raise TypeError("not all elements are lists")

    for p in paths_list:

        if type(p) is not list:

            raise TypeError(f"got path {p} which is not a list")

        if p[0] != "START":

            raise ValueError(f"got path not starting at start; {p}")

        if p[len(p) - 1] != "END":

            raise ValueError(f"got path not ending at end; {p}")

        cave_counts = Counter(p)

        if cave_counts["START"] != 1:

            raise ValueError(f"got path not visiting start once; {p}")

        if cave_counts["END"] != 1:

            raise ValueError(f"got path not visiting end once; {p}")

        for cave in cave_counts.keys():

            if cave.islower():

                if cave_counts[cave] > 1:

                    raise ValueError(
                        f"got path visiting small cave more than once; {p}"
                    )


if __name__ == "__main__":

    input = load_input("input_1.txt")

    result = count_paths_not_visiting_small_caves_twice(input)

    print(result)
