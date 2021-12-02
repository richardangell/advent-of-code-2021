import sys

sys.path.append("..")
import helpers  # noqa


def count_depth_measurement_increases(input):
    """Function to calculate the number of time depth increases between
    subsequent 3 moving average measurements.
    """

    n = len(input)

    counter = 0

    for i in range(n - 3):

        moving_average_1_lower = i
        moving_average_1_upper = i + 2 + 1

        moving_average_2_lower = i + 1
        moving_average_2_upper = i + 3 + 1

        if sum(input[moving_average_2_lower:moving_average_2_upper]) > sum(
            input[moving_average_1_lower:moving_average_1_upper]
        ):

            counter += 1

    return counter


if __name__ == "__main__":

    inputs = helpers.load_input(
        "input_1.txt", remove_lines_breaks=True, convert_to_int=True
    )

    result = count_depth_measurement_increases(inputs)

    print(result)
