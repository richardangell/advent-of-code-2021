import sys

sys.path.append("..")
import helpers  # noqa


def load_input(file: str) -> list[str]:
    """Load the input file."""

    return helpers.load_input(file, remove_lines_breaks=True)


if __name__ == "__main__":

    input = load_input("input_1.txt")

    print(input)
