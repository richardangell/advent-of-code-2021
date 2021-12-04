import puzzle_2


def test_puzzle_1():

    input_1 = puzzle_2.helpers.load_input("tests/input_1.txt", remove_lines_breaks=True)

    assert puzzle_2.calculate_oxygen_and_co2(input_1) == (23, 10)
