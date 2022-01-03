import puzzle_1

import pytest


@pytest.fixture
def input_1():

    input_1 = puzzle_1.load_input("tests/input_1.txt")

    return input_1


@pytest.fixture
def load_input():
    def _load_input(file: str):

        return puzzle_1.load_input(f"tests/{file}.txt")

    return _load_input
