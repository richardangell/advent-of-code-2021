import numpy as np
from numpy.typing import ArrayLike

import puzzle_1


def find_largest_basins(input: list[list[int]]) -> int:
    """Find the top 3 largest basins and multiply their sizes together."""

    arr = np.array(input)

    low_pints = find_low_point_coords(arr)

    basin_sizes = [
        len(find_basin_around_low_point(low_point_coord, arr))
        for low_point_coord in low_pints
    ]

    largest_basins = sorted(basin_sizes, reverse=True)[:3]

    result = largest_basins[0] * largest_basins[1] * largest_basins[2]

    return result


def find_basin_around_low_point(coords: list[int], arr: ArrayLike) -> list[list[int]]:
    """Find the coordinates of the basin around the passed low point."""

    basin_coords = [coords]

    arr[coords[0], coords[1]] = 9

    basin_coords = find_adjacent_coords_in_basin(
        coords[0], coords[1], arr, basin_coords
    )

    return basin_coords


def find_adjacent_coords_in_basin(
    x: int, y: int, arr: ArrayLike, basin: list[list[int]]
) -> list[list[int]]:
    """Recursively find the extent of the adjacent coords that belong to the basin
    lined by height 9 coords.
    """

    if x + 1 < arr.shape[0] and arr[x + 1, y] < 9:

        arr[x + 1, y] = 9

        basin.append([x + 1, y])

        find_adjacent_coords_in_basin(x + 1, y, arr, basin)

    if y + 1 < arr.shape[1] and arr[x, y + 1] < 9:

        arr[x, y + 1] = 9

        basin.append([x, y + 1])

        find_adjacent_coords_in_basin(x, y + 1, arr, basin)

    if x - 1 >= 0 and arr[x - 1, y] < 9:

        arr[x - 1, y] = 9

        basin.append([x - 1, y])

        find_adjacent_coords_in_basin(x - 1, y, arr, basin)

    if y - 1 >= 0 and arr[x, y - 1] < 9:

        arr[x, y - 1] = 9

        basin.append([x, y - 1])

        find_adjacent_coords_in_basin(x, y - 1, arr, basin)

    return basin


def find_low_point_coords(arr: ArrayLike) -> list[list[int]]:
    """Return the low point locations in the input."""

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

    low_point_coords = np.column_stack(np.where(arr_zeros == 4))

    return low_point_coords.tolist()


if __name__ == "__main__":

    input = puzzle_1.load_input("input_1.txt")

    result = find_largest_basins(input)

    print(result)
