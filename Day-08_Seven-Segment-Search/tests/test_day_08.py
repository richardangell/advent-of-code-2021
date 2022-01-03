import puzzle_1
import puzzle_2


def test_puzzle_1(input_1):

    assert puzzle_1.unique_digits_in_output(input_1) == 26


def test_puzzle_2(input_1):

    assert puzzle_2.sum_output_values(input_1) == 61229
