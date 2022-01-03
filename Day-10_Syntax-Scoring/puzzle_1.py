from typing import Union
import sys

sys.path.append("..")
import helpers  # noqa


def load_input(file: str) -> list[str]:
    """Load input file."""

    return helpers.load_input(file, remove_lines_breaks=True)


def find_error_character(chunk: str) -> Union[str, None]:
    """Find the first illegal character for a given chunk."""

    stack = []

    bracket_mapping = {")": "(", "]": "[", "}": "{", ">": "<"}

    open_brackets = ["(", "[", "{", "<"]

    for char in chunk:

        if char in open_brackets:

            stack.append(char)

        else:

            top_char = stack.pop()

            if top_char != bracket_mapping[char]:

                return char

    return None


def find_syntax_error_score(input: list[str]) -> int:
    """Find the syntax error score given by the sum of all the scores for the
    first illegal character in each chunk.
    """

    syntax_error_values = {")": 3, "]": 57, "}": 1197, ">": 25137}

    syntax_error_score = 0

    for chunk in input:

        illegal_character = find_error_character(chunk)

        if illegal_character is not None:

            syntax_error_score += syntax_error_values[illegal_character]

    return syntax_error_score


if __name__ == "__main__":

    input = load_input("input_1.txt")

    result = find_syntax_error_score(input)

    print(result)
