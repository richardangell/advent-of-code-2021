from collections import Counter
import sys

sys.path.append("..")
import helpers  # noqa


def load_input(file: str) -> tuple[str, dict[str, str]]:
    """Load the input file and return the polymer template and pair insertion rules."""

    input = helpers.load_input(file, remove_lines_breaks=True)

    polymer_template = input[0]

    input.remove(polymer_template)
    input.remove("")

    pair_insertion_rules = [split_pair_insertion_rules(rule) for rule in input]

    pair_insertion_rules_dict = {rule[0]: rule[1] for rule in pair_insertion_rules}

    return polymer_template, pair_insertion_rules_dict


def split_pair_insertion_rules(rule: str) -> tuple[str, str]:
    """Split pair insertion rule of the form 'XY -> Z' and return in the form 'XY', 'XZ'."""

    mapping = rule.split(" -> ")

    return mapping[0], mapping[0][0] + mapping[1]


def find_output_polymer(input_polymer: str, rules: dict, steps: int) -> str:
    """Progress the polymer through a given number of steps using the provided
    insertion rules.
    """

    polymer = input_polymer
    insertion_rules = rules

    for _ in range(steps):

        polymer, insertion_rules = expand_polymer(polymer, insertion_rules)

    return polymer


def expand_polymer(polymer: str, rules: dict) -> tuple[str, dict]:
    """Expand polymer with given insertion rules."""

    start_index = 0

    expanded_polymer = ""

    # to hold the expansion mapping from the previous iteration of the outermost while loop below
    previous_expansion_from = ""
    previous_expansion_to = ""

    # loop through the whole of the polymer until the last element
    while start_index < len(polymer) - 1:

        check_length = 2

        # start at length 2 and increase the length of polymer to check if there exists a mapping
        # i.e. find the maximum length of polymer for which insertion mapping exists
        while polymer[start_index : start_index + check_length + 1] in rules.keys():

            # also check if the length of polymer to check has extended past outside bounds
            if start_index + check_length + 1 > len(polymer) - 1:
                break

            check_length += 1

        # the elements to be expanded / have others inserted into
        expansion_from = polymer[start_index : start_index + check_length]

        # expansion_from after being expanded
        expansion_to = rules[expansion_from]

        expanded_polymer += expansion_to

        # add a new insertion rule which is the previous expansion + the current expansion
        # as we move from left to right across the polymer
        # note, expansion_from has the first element remove to prevent duplicating as
        # the last element of previous_expansion_from should be the same
        # note, for the first iteration of this while loop we will be overwriting an existing
        # rule with itself
        if start_index > 0:
            rules[previous_expansion_from + expansion_from[1:]] = (
                previous_expansion_to + expansion_to
            )

        # record current expansion for the next loop
        previous_expansion_to = expansion_to
        previous_expansion_from = expansion_from

        # for the next iteration start from the last element that was included in the current check
        start_index = start_index + check_length - 1

    # add the last element on from the input as this never changes
    expanded_polymer += polymer[len(polymer) - 1]

    rules[polymer] = expanded_polymer

    return expanded_polymer, rules


def find_most_common_minus_least_common_element(
    start_polymer: str, insertion_rules: dict, n: int
) -> int:
    """Find the difference between count of the most common and count of the
    least common element in the given polymer after n steps.
    """

    final_polymer = find_output_polymer(start_polymer, insertion_rules, n)

    counts = Counter([element for element in final_polymer])

    current_max = 0
    current_min = len(final_polymer)

    for element in counts.keys():

        if counts[element] > current_max:

            current_max = counts[element]

        if counts[element] < current_min:

            current_min = counts[element]

    return current_max - current_min


if __name__ == "__main__":

    polymer_template, pair_insertion_rules = load_input("input_1.txt")

    result = find_most_common_minus_least_common_element(
        polymer_template, pair_insertion_rules, 10
    )

    print(result)
