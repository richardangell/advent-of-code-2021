import puzzle_1
import puzzle_2


def test_puzzle_1():

    input_1 = puzzle_1.helpers.load_input("tests/data_1.txt", True, True)

    assert puzzle_1.count_depth_measurement_increases(input_1) == 7


def test_puzzle_2():

    input_1 = puzzle_2.helpers.load_input("tests/data_1.txt", True, True)

    assert puzzle_2.count_depth_measurement_increases(input_1) == 5
