import puzzle_1
import puzzle_2

import pytest


@pytest.fixture
def input_1():

    input_1 = puzzle_1.load_input("tests/input_1.txt")

    return input_1


@pytest.fixture
def input_1_pt2():

    input_1 = puzzle_2.load_input("tests/input_1.txt")

    return input_1
