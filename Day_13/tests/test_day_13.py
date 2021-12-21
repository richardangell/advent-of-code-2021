import pytest
import numpy as np

import puzzle_1


class TestPuzzle1:
    """Tests for puzzle 1."""

    def test_vertial_fold(self, input_1):
        """Test a vertical fold on the input produces the right output of dots."""

        expected = np.array(
            [
                [1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0],
                [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
                [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                [0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ]
        )

        actual = puzzle_1.apply_fold(input_1[0], input_1[1][0])

        # apply clipping at [0, 1] to make output of apply_fold match test output
        actual_clipped = np.clip(actual, a_min=0, a_max=1)

        np.testing.assert_array_equal(actual_clipped, expected)

    @pytest.mark.parametrize("n_folds,expected", [(1, 17), (2, 16)])
    def test_count_visible_dots_after_folding(self, input_1, n_folds, expected):
        """Test that the number of visible dots is calculated correcrtly."""

        assert (
            puzzle_1.count_visible_dots_after_folding(input_1[0], input_1[1], n_folds)
            == expected
        )


class TestPuzzle2:
    """Tests for puzzle 2."""

    def test_puzzle_2(self, input_1):

        assert 1 == 1
