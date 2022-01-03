from numpy.typing import ArrayLike
import puzzle_1


def find_synchronisation_step(starting_state: ArrayLike) -> int:
    """Find the first step after which all octopuses flash together."""

    n_steps = 0

    state = starting_state

    while state.sum() > 0:

        n_steps += 1

        state, _ = puzzle_1.progress_step(state)

        if n_steps > 500:

            raise ValueError("large number of steps reached")

    return n_steps


if __name__ == "__main__":

    input = puzzle_1.load_input("input_1.txt")

    result = find_synchronisation_step(input)

    print(result)
