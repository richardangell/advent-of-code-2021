import numpy as np
from numpy.typing import ArrayLike

import puzzle_1


def cap_result(paper: ArrayLike) -> ArrayLike:
    """Cap values in array at [0,1]."""

    return np.clip(paper, a_min=0, a_max=1).astype(int)


if __name__ == "__main__":

    paper, fold_instructions = puzzle_1.load_input("input_1.txt")

    result = puzzle_1.fold_paper(paper, fold_instructions, len(fold_instructions))

    result_capped = cap_result(result)

    np.set_printoptions(linewidth=180)
    print(result_capped)
