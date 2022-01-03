import puzzle_1

import pytest


@pytest.fixture
def load_input():
    def _load_input(file: str):

        return puzzle_1.load_input(f"tests/{file}.txt")

    return _load_input


@pytest.fixture
def load_output():
    def _load_output(file: str):

        return puzzle_1.helpers.load_input_split(
            f"tests/{file}.txt", remove_lines_breaks=True, split_string=","
        )

    return _load_output
