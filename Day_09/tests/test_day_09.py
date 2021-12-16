import numpy as np
import pytest

import puzzle_1
import puzzle_2


class TestPuzzle1:
    """Tests for puzzle 1."""

    def test_low_point_heights(self, input_1):
        """Test that the heights of low points are correct."""

        assert puzzle_1.find_low_point_heights(input_1) == [1, 0, 5, 5]

    def test_find_risk_level_sum(self, input_1):
        """Test the sum of risk levels are correct."""

        assert puzzle_1.find_risk_level_sum(input_1) == 15


class TestPuzzle2:
    """Tests for puzzle 2."""

    def test_find_largest_basins(self, input_1):
        """Test that the overall solution find_largest_basins is correct."""

        assert puzzle_2.find_largest_basins(input_1) == 1134

    @pytest.mark.parametrize(
        "coords,expected",
        [
            ([0, 1], [[0, 0], [0, 1], [1, 0]]),
            (
                [0, 9],
                [
                    [0, 5],
                    [0, 6],
                    [0, 7],
                    [0, 8],
                    [0, 9],
                    [1, 6],
                    [1, 8],
                    [1, 9],
                    [2, 9],
                ],
            ),
            (
                [2, 2],
                [
                    [1, 2],
                    [1, 3],
                    [1, 4],
                    [2, 1],
                    [2, 2],
                    [2, 3],
                    [2, 4],
                    [2, 5],
                    [3, 0],
                    [3, 1],
                    [3, 2],
                    [3, 3],
                    [3, 4],
                    [4, 1],
                ],
            ),
            (
                [4, 6],
                [
                    [2, 7],
                    [3, 6],
                    [3, 7],
                    [3, 8],
                    [4, 5],
                    [4, 6],
                    [4, 7],
                    [4, 8],
                    [4, 9],
                ],
            ),
        ],
    )
    def test_find_basin_around_low_point(self, input_1, coords, expected):

        arr = np.array(input_1)

        result = puzzle_2.find_basin_around_low_point(coords, arr)

        assert sorted(expected) == sorted(result)
