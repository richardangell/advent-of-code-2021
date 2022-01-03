import puzzle_1

from collections import Counter
import sys

sys.path.append("..")
import helpers  # noqa


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

        distance_moved = abs(align_position - position)

        distance_moved_cost = (distance_moved * (distance_moved + 1)) / 2

        fuel_cost += distance_moved_cost * count

    return int(fuel_cost)


if __name__ == "__main__":

    input = puzzle_1.load_input("input_1.txt")

    result = find_minimum_fuel_for_alignment(input)

    print(result)
