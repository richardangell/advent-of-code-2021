def load_input(file, remove_lines_breaks=False, convert_to_int=False):
    """Function to load input with optional processing."""

    with open(file) as f:

        lines = f.readlines()

    if remove_lines_breaks:

        lines = [x.replace("\n", "") for x in lines]

    if convert_to_int:

        lines = [int(x) for x in lines]

    return lines
