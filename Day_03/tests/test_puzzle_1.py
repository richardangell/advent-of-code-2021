import puzzle_1


def test_puzzle_1():

    input_1 = puzzle_1.helpers.load_input("tests/input_1.txt", remove_lines_breaks=True)

    assert puzzle_1.calculate_gamma_and_epsilon(input_1) == (22, 9)
