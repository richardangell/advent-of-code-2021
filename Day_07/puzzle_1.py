from collections import Counter
import sys

sys.path.append("..")
import helpers  # noqa


def load_input(file: str) -> list[int]:
    """Load input file."""

    input = helpers.load_input(file, remove_lines_breaks=True)

    input_processed = [int(x) for x in input[0].split(",")]

    return input_processed


def find_minimum_fuel_for_alignment(input: list[int]) -> int:
    """Find the minimum amount of fuel to horizontally align crabs."""

    initial_positions = Counter(input)

    min_horizontal_position = min(input)
    max_horizontal_position = max(input)

    fuel_costs = [
        find_fuel_for_alignment(initial_positions, pos)
        for pos in range(min_horizontal_position, max_horizontal_position + 1)
    ]

    min_fuel_cost = min(fuel_costs)

    return min_fuel_cost


def find_fuel_for_alignment(position_counts: Counter, align_position: int) -> int:
    """Find the fuel required to align at the given horizontal position."""

    fuel_cost = 0

    for position, count in position_counts.items():

        fuel_cost += abs(align_position - position) * count

    return fuel_cost


if __name__ == "__main__":

    input = load_input("input_1.txt")

    result = find_minimum_fuel_for_alignment(input)

    print(result)
