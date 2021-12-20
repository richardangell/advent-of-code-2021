"""Helper module with data loading functions that can be reused for
each puzzle.
"""


def load_input(file: str, remove_lines_breaks: bool = False) -> list[str]:
    """Function to load input with optional removal of line breaks."""

    with open(file) as f:

        lines = f.readlines()

    if remove_lines_breaks:

        lines_processed = [x.replace("\n", "") for x in lines]

        return lines_processed

    else:

        return lines


def load_input_int(file: str, remove_lines_breaks: bool = False) -> list[int]:
    """Function to load input and convert each line to int."""

    lines = load_input(file, remove_lines_breaks)

    lines_processed = [int(x) for x in lines]

    return lines_processed


def load_input_split(
    file: str, remove_lines_breaks: bool = False, split_string: str = " "
) -> list[list[str]]:
    """Function to load input and split each line by a space separator."""

    lines = load_input(file, remove_lines_breaks)

    lines_processed = [x.split(split_string) for x in lines]

    return lines_processed
