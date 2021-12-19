import numpy as np
from numpy.typing import ArrayLike
import sys

sys.path.append("..")
import helpers  # noqa


def load_input(file: str) -> ArrayLike:
    """Load the input file."""

    input = helpers.load_input(file, remove_lines_breaks=True)

    input_split = [[int(x) for x in row] for row in input]

    return np.array(input_split)


def progress_step(state: ArrayLike, limit: int = 10) -> tuple[ArrayLike, int]:
    """Progress the octopus grid state by one step."""

    # increase energy level of all octopus by 1
    state = state + 1

    flashed_octopuses = get_flashes(state)

    new_flashes = flashed_octopuses

    flashes = len(new_flashes)

    while flashes > 0:

        all_adjacent_octopuses = []

        for octopus in new_flashes:

            all_adjacent_octopuses.extend(get_adjacent_octopus(octopus, limit))

        # find adjacent octopuses
        # get unique octopuses adjacent to flashes and remove the flashed octopuses
        # adjacent_octopuses = set(all_adjacent_octopuses) - flashed_octopuses
        # import pdb; pdb.set_trace()
        for octopus in all_adjacent_octopuses:

            if octopus not in flashed_octopuses:

                state[octopus[0], octopus[1]] = state[octopus[0], octopus[1]] + 1

        flashed_octopuses_temp = get_flashes(state)

        new_flashes = flashed_octopuses_temp - flashed_octopuses

        flashed_octopuses = flashed_octopuses_temp

        flashes = len(new_flashes)

    # reset state to 0 for any octopus that flash
    state[state > 9] = 0

    flashes = len(flashed_octopuses)

    return state, flashes


def get_flashes(state: ArrayLike) -> set[tuple[int, ...]]:
    """Find octopuses that flash by having an energy level > 9."""

    return set([tuple(x) for x in np.column_stack(np.where(state > 9)).tolist()])


def get_adjacent_octopus(
    octopus: tuple[int, ...], limit: int = 10
) -> list[tuple[int, ...]]:
    """Return the octopus that are adjacent to the input octopus given
    theere are 10x10 in a grid.
    """

    adjacent_octopus: list = []

    x = octopus[0]
    y = octopus[1]

    if x < limit - 1:

        adjacent_octopus.append((x + 1, y))

        if y < limit - 1:

            adjacent_octopus.append((x + 1, y + 1))

        if y > 0:

            adjacent_octopus.append((x + 1, y - 1))

    if x > 0:

        adjacent_octopus.append((x - 1, y))

        if y < limit - 1:

            adjacent_octopus.append((x - 1, y + 1))

        if y > 0:

            adjacent_octopus.append((x - 1, y - 1))

    if y < limit - 1:

        adjacent_octopus.append((x, y + 1))

    if y > 0:

        adjacent_octopus.append((x, y - 1))

    return adjacent_octopus


def calculate_flashes(starting_state: ArrayLike, steps: int) -> tuple[ArrayLike, int]:
    """Calculate the number of octopus flashes after a given number of steps."""

    flashes_count = 0

    state = starting_state

    for _ in range(steps):

        state, count = progress_step(state)

        flashes_count += count

    return state, flashes_count


if __name__ == "__main__":

    input = load_input("input_1.txt")

    _, result = calculate_flashes(input, 100)

    print(result)
