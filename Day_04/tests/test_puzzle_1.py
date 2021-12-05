import puzzle_1


def test_puzzle_1():

    input_1 = puzzle_1.load_input("tests/input_1.txt")

    assert puzzle_1.calculate_winning_score(*input_1) == (4512, 188, 24)
