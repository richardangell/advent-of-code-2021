import numpy as np
from numpy.typing import ArrayLike
import puzzle_1


def load_input(file: str) -> ArrayLike:
    """Load the puzzle input and duplicate 5 times in each direction,
    adding 1 to the array for each copy.
    """

    input = puzzle_1.load_input(file)

    input_1x5 = np.copy(input)

    for _ in range(4):

        input = np.clip(np.mod(input + 1, 10), a_min=1, a_max=None)

        input_1x5 = np.concatenate([input_1x5, input], axis=1)

    input_5x5 = np.copy(input_1x5)

    for _ in range(4):

        input_1x5 = np.clip(np.mod(input_1x5 + 1, 10), a_min=1, a_max=None)

        input_5x5 = np.concatenate([input_5x5, input_1x5], axis=0)

    return input_5x5


if __name__ == "__main__":

    input = load_input("input_1.txt")

    result = puzzle_1.find_lowest_risk_score(input)

    print(result)
