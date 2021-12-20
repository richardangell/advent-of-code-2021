import pytest

import puzzle_1
import puzzle_2


class TestPuzzle1:
    """Tests for puzzle 1."""

    @pytest.mark.parametrize(
        "input_file,expected", [("input_1", 10), ("input_2", 19), ("input_3", 226)]
    )
    def test_count_paths_not_visiting_small_caves_twice(
        self, load_input, input_file, expected
    ):
        """Test that the count of paths found is correct."""

        input = load_input(input_file)

        assert puzzle_1.count_paths_not_visiting_small_caves_twice(input) == expected

    @pytest.mark.parametrize(
        "input_file,output_file",
        [("input_1", "input_1_output"), ("input_2", "input_2_output")],
    )
    def test_paths_found(self, load_input, load_output, input_file, output_file):
        """Test that the correct paths are found."""

        input = load_input(input_file)
        output = load_output(output_file)

        input_processed = puzzle_1.process_input(input)

        nested_paths = puzzle_1.find_paths_not_visiting_small_caves_twice(
            input_processed
        )

        result = puzzle_1.unnest_paths(nested_paths)

        assert sorted(result) == sorted(output)


class TestPuzzle2:
    """Tests for puzzle 2."""

    def test_paths_found(self, load_input, load_output):
        """Test that the correct paths are found."""

        input = load_input("input_1")
        output = load_output("input_1_output_pt_2")

        input_processed = puzzle_1.process_input(input)

        nested_paths = puzzle_2.find_allowed_paths(input_processed)

        result = puzzle_1.unnest_paths(nested_paths)

        assert sorted(result) == sorted(output)

    @pytest.mark.parametrize(
        "input_file,expected", [("input_1", 36), ("input_2", 103), ("input_3", 3509)]
    )
    def test_count_allowed_paths(self, load_input, input_file, expected):
        """Test that the count of paths found is correct."""

        input = load_input(input_file)

        assert puzzle_2.count_allowed_paths(input) == expected
