import numpy as np
from numpy.typing import ArrayLike
import sys

sys.path.append("..")
import helpers  # noqa


def load_input(file: str) -> tuple:
    """Load the input file and return an array of the dots and the fold
    instructions.
    """

    input = helpers.load_input(file, remove_lines_breaks=True)

    folds = []

    while True:

        item = input.pop()

        if item == "":

            break

        folds.append(item)

    fold_info = [split_fold_input_row(fold) for fold in reversed(folds)]

    coord_info = [[int(coord) for coord in row.split(",")] for row in input]

    dots = create_array_from_coords(coord_info)

    return dots, fold_info


def split_fold_input_row(row: str) -> tuple:
    """Split fold information in the input."""

    row_split = row.split("=")

    if "x" in row_split[0]:

        axis = "x"

    elif "y" in row_split[0]:

        axis = "y"

    else:

        raise ValueError("axis not found")

    value = int(row_split[1])

    return axis, value


def create_array_from_coords(coords: list[list[int]]) -> ArrayLike:
    """Create a binary array with 1s in locations of the coordinates passed."""

    max_x = 0
    max_y = 0

    for coord in coords:

        if coord[0] > max_x:

            max_x = coord[0]

        if coord[1] > max_y:

            max_y = coord[1]

    dot_array = np.zeros((max_y + 2, max_x + 1))

    for coord in coords:

        dot_array[coord[1], coord[0]] = 1

    return dot_array


def fold_paper(
    paper: ArrayLike, instructions: list[tuple[str, int]], n: int
) -> ArrayLike:
    """Fold paper with dots following the first n fold instructions only."""

    for fold_no in range(n):

        paper = apply_fold(paper, instructions[fold_no])

    return paper


def count_visible_dots_after_folding(
    paper: ArrayLike, instructions: list[tuple[str, int]], n: int
) -> int:
    """Count the number of visible dots after applying the first n fold instructions only."""

    folded_paper = fold_paper(paper, instructions, n)

    n_visible_dots = (folded_paper >= 1).sum()

    return n_visible_dots


def apply_fold(paper: ArrayLike, instruction: tuple[str, int]) -> ArrayLike:
    """Apply a single fold instruction to the input paper."""

    axis = instruction[0]
    fold_point = instruction[1]

    # left fold
    if axis == "x":

        left_half = paper[:, :(fold_point)]
        right_half = paper[:, (fold_point + 1) :]

        right_flipped = np.flip(right_half, axis=1)

        return left_half + right_flipped

    # up fold
    elif axis == "y":

        top_half = paper[:(fold_point), :]
        bottom_half = paper[(fold_point + 1) :, :]

        bottom_flipped = np.flip(bottom_half, axis=0)

        return top_half + bottom_flipped

    else:

        raise ValueError(f"unexpected axis to fold along {instruction[0]}")


if __name__ == "__main__":

    paper, fold_instructions = load_input("input_1.txt")

    result = count_visible_dots_after_folding(paper, fold_instructions, 1)

    print(result)
