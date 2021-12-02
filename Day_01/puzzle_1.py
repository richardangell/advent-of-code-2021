import sys

sys.path.append("..")
import helpers  # noqa


def count_depth_measurement_increases(input):
    """Function to calculate the number of time depth increases between
    subsequent measurements.
    """

    n = len(input)

    counter = 0

    for i in range(n - 1):

        if input[i + 1] > input[i]:

            counter += 1

    return counter


if __name__ == "__main__":

    inputs = helpers.load_input(
        "input_1.txt", remove_lines_breaks=True, convert_to_int=True
    )

    result = count_depth_measurement_increases(inputs)

    print(result)