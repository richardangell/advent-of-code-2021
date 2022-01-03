import puzzle_1

import pytest


@pytest.fixture
def load_octopuses():
    def _load_octopuses(file: str):

        return puzzle_1.load_input(f"tests/{file}.txt")

    return _load_octopuses
