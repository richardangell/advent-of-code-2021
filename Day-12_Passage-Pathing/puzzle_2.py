from collections import Counter

import puzzle_1


def find_allowed_paths(input: dict) -> list[list[str]]:
    """Find all the unique paths that can visit one small cave at most twice
    and the rest at most once.
    """

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

    small_caves = [cave for cave in previous_cave_counts.keys() if cave.islower()]

    any_small_cave_visited_twice = any(
        [previous_cave_counts[cave] > 1 for cave in small_caves]
    )

    if any_small_cave_visited_twice:

        small_caves_to_remove = [
            cave for cave in small_caves if previous_cave_counts[cave] > 0
        ]

    else:

        small_caves_to_remove = []

    potential_next_caves = [
        cave_ for cave_ in cave_system[cave] if cave_ not in small_caves_to_remove
    ]

    if len(potential_next_caves) > 0:

        return [
            traverse_caves_recursive(next_cave, cave_system, current_path)
            for next_cave in potential_next_caves
        ]


def count_allowed_paths(input: list[list[str]]) -> int:
    """Find the number of paths that visit at most one small caves twice
    but the rest at most once.
    """

    input_processed = puzzle_1.process_input(input)

    nested_paths = find_allowed_paths(input_processed)

    paths = puzzle_1.unnest_paths(nested_paths)

    return len(paths)


if __name__ == "__main__":

    input = puzzle_1.load_input("input_1.txt")

    result = count_allowed_paths(input)

    print(result)
