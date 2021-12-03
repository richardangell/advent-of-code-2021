import sys

sys.path.append("..")
import helpers  # noqa


def calculate_position_and_depth(input):
    """Function to horizontal and position from direction instructions."""

    horizontal_location = 0
    depth = 0
    aim = 0

    for x in input:

        instruction = x[0]
        magnitude = int(x[1])

        match instruction:
            case "forward":
                horizontal_location += magnitude
                depth += aim * magnitude
            case "down":
                aim += magnitude
            case "up":
                aim -= magnitude
            case _:
                raise ValueError(f"unexpected instruction; {instruction}")

    return horizontal_location, depth


if __name__ == "__main__":

    inputs = helpers.load_input(
        "input_1.txt", remove_lines_breaks=True, split_lines=True
    )

    result = calculate_position_and_depth(inputs)

    print(result, result[0] * result[1])
