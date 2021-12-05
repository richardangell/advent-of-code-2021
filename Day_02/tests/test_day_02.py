import puzzle_1
import puzzle_2


def test_puzzle_1():

    input_1 = puzzle_1.helpers.load_input(
        "tests/input_1.txt", remove_lines_breaks=True, split_lines=True
    )

    assert puzzle_1.calculate_position_and_depth(input_1) == (15, 10)


def test_puzzle_2():

    input_1 = puzzle_2.helpers.load_input(
        "tests/input_1.txt", remove_lines_breaks=True, split_lines=True
    )

    assert puzzle_2.calculate_position_and_depth(input_1) == (15, 60)
