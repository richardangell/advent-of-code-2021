from numpy.testing import assert_array_equal
import pytest

import puzzle_1
import puzzle_2


class TestPuzzle1:
    """Tests for puzzle 1."""

    @pytest.mark.parametrize(
        "input,steps,expected_output",
        [("input_1", 1, "input_1_output_1"), ("input_1", 2, "input_1_output_2")],
    )
    def test_progress_step_small(self, load_octopuses, input, steps, expected_output):
        """Test progress_step on 5x5 input."""

        input_octopuses = load_octopuses(input)
        expected_output_octopuses = load_octopuses(expected_output)

        actual = input_octopuses

        for _ in range(steps):

            actual, _ = puzzle_1.progress_step(actual, limit=5)

        assert_array_equal(actual, expected_output_octopuses)

    @pytest.mark.parametrize(
        "input,steps,expected_output",
        [
            ("input_2", 1, "input_2_output_1"),
            ("input_2", 2, "input_2_output_2"),
            ("input_2", 3, "input_2_output_3"),
            ("input_2", 4, "input_2_output_4"),
            ("input_2", 5, "input_2_output_5"),
            ("input_2", 6, "input_2_output_6"),
            ("input_2", 7, "input_2_output_7"),
            ("input_2", 8, "input_2_output_8"),
            ("input_2", 9, "input_2_output_9"),
            ("input_2", 10, "input_2_output_10"),
            ("input_2", 20, "input_2_output_20"),
            ("input_2", 30, "input_2_output_30"),
            ("input_2", 40, "input_2_output_40"),
            ("input_2", 50, "input_2_output_50"),
            ("input_2", 60, "input_2_output_60"),
            ("input_2", 70, "input_2_output_70"),
            ("input_2", 80, "input_2_output_80"),
            ("input_2", 90, "input_2_output_90"),
            ("input_2", 100, "input_2_output_100"),
        ],
    )
    def test_progress_step_large(self, load_octopuses, input, steps, expected_output):
        """Test progress_step on 10x10 input."""

        input_octopuses = load_octopuses(input)
        expected_output_octopuses = load_octopuses(expected_output)

        actual = input_octopuses

        for _ in range(steps):

            actual, _ = puzzle_1.progress_step(actual)

        assert_array_equal(actual, expected_output_octopuses)

    @pytest.mark.parametrize(
        "expected,steps", [(0, 1), (35, 2), (80, 3), (96, 4), (1656, 100)]
    )
    def test_calculate_flashes_large(self, load_octopuses, steps, expected):
        """Test calculate_flashes on 10x10 input."""

        input_octopuses = load_octopuses("input_2")

        _, output = puzzle_1.calculate_flashes(input_octopuses, steps)

        assert output == expected


class TestPuzzle2:
    """Tests for puzzle 2."""

    def test_find_synchronisation_step(self, load_octopuses):

        octopuses = load_octopuses("input_2")

        assert puzzle_2.find_synchronisation_step(octopuses) == 195
