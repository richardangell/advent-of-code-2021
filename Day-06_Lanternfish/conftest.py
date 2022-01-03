import puzzle_1

import pytest


@pytest.fixture
def input_1():

    input_1 = puzzle_1.load_input("tests/input_1.txt")

    return input_1
