from collections import Counter
import sys

sys.path.append("..")
import helpers  # noqa


def load_input(file: str) -> tuple[str, dict[str, list[str]]]:
    """Load the input file and return the polymer template and pair insertion rules."""

    input = helpers.load_input(file, remove_lines_breaks=True)

    polymer_template = input[0]

    input.remove(polymer_template)
    input.remove("")

    pair_insertion_rules = [split_pair_insertion_rules(rule) for rule in input]

    pair_insertion_rules_dict = {rule[0]: rule[1] for rule in pair_insertion_rules}

    return polymer_template, pair_insertion_rules_dict


def split_pair_insertion_rules(rule: str) -> tuple[str, list[str]]:
    """Split pair insertion rule of the form 'XY -> Z' and return in the form 'XY', ['XZ', 'ZY']."""

    mapping = rule.split(" -> ")

    return mapping[0], [mapping[0][0] + mapping[1], mapping[1] + mapping[0][1]]


def find_most_common_minus_least_common_element(
    start_polymer: str, insertion_rules: dict, n: int
) -> int:
    """Find the difference between count of the most common and count of the
    least common element in the given polymer after n steps.
    """

    pair_counter = count_polymer_pairs_steps(start_polymer, insertion_rules, n)

    single_counter: Counter = Counter()

    # add count for second character in each pair only i.e. remove the first
    # to account for overlapping characters between adjacent pairs
    for pair, counts in pair_counter.items():

        single_counter[pair[1]] += counts

    # add the first element back on, as this never changes but is removed above
    single_counter[start_polymer[0]] += 1

    least_count = min([single_counter[element] for element in single_counter.keys()])
    most_count = max([single_counter[element] for element in single_counter.keys()])

    return most_count - least_count


def count_polymer_pairs_steps(input_polymer: str, rules: dict, steps: int) -> Counter:
    """Count the number of each pair of elements in the polymer after progressing a
    given number of steps.
    """

    # create initial counts of element pairs
    pair_counts = Counter(
        [input_polymer[i : i + 2] for i in range(len(input_polymer) - 1)]
    )

    for i in range(steps):

        pair_counts = count_polymer_pairs(pair_counts, rules)

    return pair_counts


def count_polymer_pairs(counts: Counter, rules: dict) -> Counter:
    """Count the number of element pairs in the next step for the polymer."""

    new_step_counts: Counter = Counter()

    for pair, pair_count in counts.items():

        if pair_count > 0:

            for new_pair in rules[pair]:

                new_step_counts[new_pair] += counts[pair]

    return new_step_counts


if __name__ == "__main__":

    polymer_template, pair_insertion_rules = load_input("input_1.txt")

    result = find_most_common_minus_least_common_element(
        polymer_template, pair_insertion_rules, 40
    )

    print(result)
