import sys

sys.path.append("..")
import helpers  # noqa


def load_input(file: str) -> list[tuple[list[str], ...]]:
    """Load the input file."""

    input = helpers.load_input(file, remove_lines_breaks=True)

    input_processed = [
        tuple([signal_pattern.split(" ") for signal_pattern in line.split(" | ")])
        for line in input
    ]

    return input_processed


def unique_digits_in_output(input: list[tuple[list[str], ...]]) -> int:
    """Count the number of times 1, 4, 7 and 8 appear in the output
    given the number of segments that must be present to produce that
    number on a seven segment display.
    """

    count = 0

    for signal_pattern in input:

        for digit in signal_pattern[1]:

            if len(digit) in [2, 3, 4, 7]:

                count += 1

    return count


if __name__ == "__main__":

    input = load_input("input_1.txt")

    result = unique_digits_in_output(input)

    print(result)
