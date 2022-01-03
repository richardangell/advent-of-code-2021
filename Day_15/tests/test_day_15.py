import puzzle_1
import puzzle_2

import pytest


class TestPuzzle1:
    """Tests for puzzle 1."""

    @pytest.mark.parametrize(
        "file,expected",
        [
            ("input_1", 40),
            ("input_2", 18),
            ("input_3", 20),
            ("input_4", 10),
            ("input_5", 19),
        ],
    )
    def test_find_lowest_risk_score(self, load_input, file, expected):

        input = load_input(file)

        assert puzzle_1.find_lowest_risk_score(input) == expected


class TestPuzzle2:
    """Tests for puzzle 2."""

    def test_find_lowest_risk_score(self):

        input = puzzle_2.load_input("tests/input_1.txt")

        assert puzzle_1.find_lowest_risk_score(input) == 315
