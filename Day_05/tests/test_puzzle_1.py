import puzzle_1


def test_puzzle_1():

    input_1 = puzzle_1.load_input("tests/input_1.txt")

    assert puzzle_1.calculate_most_dangerous_points(input_1) == 5
