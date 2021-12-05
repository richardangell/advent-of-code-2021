import puzzle_2


def test_puzzle_2():

    input_1 = puzzle_2.load_input("tests/input_1.txt")

    assert puzzle_2.calculate_last_winning_score(*input_1) == (1924, 148, 13)
