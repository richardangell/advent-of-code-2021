import puzzle_1
import puzzle_2

import pytest
from collections import Counter


class TestPuzzle1:
    """Tests for puzzle 1."""

    @pytest.mark.parametrize("position,expected", [(2, 37), (1, 41), (3, 39), (10, 71)])
    def test_find_fuel_for_alignment(self, input_1, position, expected):

        assert puzzle_1.find_fuel_for_alignment(Counter(input_1), position) == expected

    def test_find_minimum_fuel_for_alignment(self, input_1):

        assert puzzle_1.find_minimum_fuel_for_alignment(input_1) == 37


class TestPuzzle2:
    """Tests for puzzle 2."""

    @pytest.mark.parametrize("position,expected", [(5, 168), (2, 206)])
    def test_find_fuel_for_alignment(self, input_1, position, expected):

        assert puzzle_2.find_fuel_for_alignment(Counter(input_1), position) == expected

    def test_find_minimum_fuel_for_alignment(self, input_1):

        assert puzzle_2.find_minimum_fuel_for_alignment(input_1) == 168
