import puzzle_1


def test_puzzle_1():

    input_1 = puzzle_1.helpers.load_input("tests/data_1.txt", True, True)

    assert puzzle_1.count_depth_measurement_increases(input_1) == 7
