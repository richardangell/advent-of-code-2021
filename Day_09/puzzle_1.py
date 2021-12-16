import numpy as np
import sys

sys.path.append("..")
import helpers  # noqa


def load_input(file: str) -> list[list[int]]:
    """Load the input and return a list of lists (of ints)."""

    input = helpers.load_input(file, remove_lines_breaks=True)

    input_split = [[int(x) for x in row] for row in input]

    return input_split


def find_risk_level_sum(input: list[list[int]]) -> int:
    """Find the sum of all risk levels in the cave map."""

    low_point_heights = find_low_point_heights(input)

    risk_levels = [height + 1 for height in low_point_heights]

    return sum(risk_levels)


def find_low_point_heights(input: list[list[int]]) -> list[int]:
    """Return the heights of all low points in the input."""

    arr = np.array(input)
    arr_zeros = np.zeros(arr.shape)

    # row[i+1] - row[i] > 0 => [row i+1] > row[i]
    diff_down = np.diff(arr, 1, axis=0)

    # row[i] - row[i+1] > 0 => row[i] > row[i+1]
    diff_up = -1 * diff_down

    # col[i+1] - col[i] > 0 => col[i+1] > col[i]
    diff_right = np.diff(arr, 1, axis=1)

    # col[i] - col[i+1] > 0 => col[i] > col[+]
    diff_left = -1 * diff_right

    # find positions where there is a decrease in height
    gt_0_down = (diff_down > 0) * 1
    gt_0_up = (diff_up > 0) * 1
    gt_0_right = (diff_right > 0) * 1
    gt_0_left = (diff_left > 0) * 1

    # add together # decreases in height moving to adjacent positions, accounting for margin
    arr_zeros[0:-1, :] = arr_zeros[0:-1, :] + gt_0_down
    arr_zeros[1:, :] = arr_zeros[1:, :] + gt_0_up
    arr_zeros[:, 0:-1] = arr_zeros[:, 0:-1] + gt_0_right
    arr_zeros[:, 1:] = arr_zeros[:, 1:] + gt_0_left

    # add on values for the edge rows/columns to save having to check == 2 or == 3
    # for corner or edge positions
    arr_zeros[0, :] = arr_zeros[0, :] + np.ones(arr_zeros.shape[1])
    arr_zeros[-1, :] = arr_zeros[-1, :] + np.ones(arr_zeros.shape[1])
    arr_zeros[:, 0] = arr_zeros[:, 0] + np.ones(arr_zeros.shape[0])
    arr_zeros[:, -1] = arr_zeros[:, -1] + np.ones(arr_zeros.shape[0])

    low_points = arr[arr_zeros == 4]

    return low_points.tolist()


if __name__ == "__main__":

    input = load_input("input_1.txt")

    result = find_risk_level_sum(input)

    print(result)
