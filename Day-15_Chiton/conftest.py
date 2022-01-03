import puzzle_1

import pytest


@pytest.fixture
def load_input():
    def _load_input(file: str):

        return puzzle_1.load_input(f"tests/{file}.txt")

    return _load_input
