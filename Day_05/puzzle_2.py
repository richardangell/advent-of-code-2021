from collections import Counter
import typing
import sys
from puzzle_1 import load_input

sys.path.append("..")
import helpers  # noqa


def calculate_most_dangerous_points(input: list[list[tuple[int, ...]]]) -> int:
    """Function to calculate the most dangerous hydrothermal
    vent locations - which have more than 2 lines crossing
    them.
    """

    path_counters = [convert_coord_pair_to_counter(x) for x in input]

    overall_counter: typing.Counter = Counter()

    for path_counter in path_counters:

        overall_counter.update(path_counter)

    danger_coords = len([i for i in overall_counter.values() if i >= 2])

    return danger_coords


def convert_coord_pair_to_counter(coord_pair: list[tuple[int, ...]]) -> typing.Counter:
    """Function to convert a list of a pair of tuples giving
    start and end coords to a Counter for each coordinate.
    """

    coord_counter: typing.Counter = Counter()

    start_coord = coord_pair[0]
    end_coord = coord_pair[1]

    if start_coord[0] < end_coord[0]:

        x_step = 1

    else:

        x_step = -1

    if start_coord[1] < end_coord[1]:

        y_step = 1

    else:

        y_step = -1

    if start_coord[0] == end_coord[0]:

        for y_coord in range(start_coord[1], end_coord[1] + y_step, y_step):

            coord_counter[(start_coord[0], y_coord)] = 1

    elif start_coord[1] == end_coord[1]:

        for x_coord in range(start_coord[0], end_coord[0] + x_step, x_step):

            coord_counter[(x_coord, start_coord[1])] = 1

    elif abs(start_coord[0] - end_coord[0]) == abs(start_coord[1] - end_coord[1]):

        for x_coord, y_coord in zip(
            range(start_coord[0], end_coord[0] + x_step, x_step),
            range(start_coord[1], end_coord[1] + y_step, y_step),
        ):

            coord_counter[(x_coord, y_coord)] = 1

    else:

        raise ValueError(f"diagonal coord pair without gradient 1 or -1; {coord_pair}")

    return coord_counter


if __name__ == "__main__":

    input = load_input("input_1.txt")

    result = calculate_most_dangerous_points(input)

    print(result)
