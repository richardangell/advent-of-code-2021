import pytest

import puzzle_1
import puzzle_2


class TestPuzzle1:
    """Tests for puzzle 1."""

    @pytest.mark.parametrize(
        "steps,expected",
        [
            (1, "NCNBCHB"),
            (2, "NBCCNBBBCBHCB"),
            (3, "NBBBCNCCNBBNBNBBCHBHHBCHB"),
            (4, "NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB"),
        ],
    )
    def test_find_output_polymer(self, input_1, steps, expected):
        """Test find_output_polymer returns the correct polymer."""

        assert puzzle_1.find_output_polymer(input_1[0], input_1[1], steps) == expected

    def test_find_most_common_minus_least_common_element(self, input_1):
        """Test find_most_common_minus_least_common_element output is correct."""

        assert (
            puzzle_1.find_most_common_minus_least_common_element(
                input_1[0], input_1[1], 10
            )
            == 1588
        )


class TestPuzzle2:
    """Tests for puzzle 2."""

    @pytest.mark.parametrize(
        "steps,expected",
        [
            (10, 1588),
            (40, 2188189693529),
        ],
    )
    def test_find_most_common_minus_least_common_element(
        self, input_1_pt2, steps, expected
    ):
        """Test find_most_common_minus_least_common_element output is correct for larger number of steps."""

        assert (
            puzzle_2.find_most_common_minus_least_common_element(
                input_1_pt2[0], input_1_pt2[1], steps
            )
            == expected
        )
