import puzzle_1
import puzzle_2


def test_puzzle_1():

    input_1 = puzzle_1.load_input("tests/input_1.txt")

    assert puzzle_1.calculate_most_dangerous_points(input_1) == 5


def test_puzzle_2():

    input_1 = puzzle_2.load_input("tests/input_1.txt")

    assert puzzle_2.calculate_most_dangerous_points(input_1) == 12
