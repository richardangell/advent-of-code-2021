import sys

sys.path.append("..")
import helpers  # noqa


def calculate_oxygen_rating(input):
    """Function to calculate oxygen rating from diagnostic report."""

    n_chars = len(input[0])

    allowed_indexes = [i for i in range(len(input))]

    for char_index in range(n_chars):

        zero_indexes = []
        one_indexes = []

        for allowed_index in allowed_indexes:

            if input[allowed_index][char_index] == "0":

                zero_indexes.append(allowed_index)

            else:

                one_indexes.append(allowed_index)

        if len(zero_indexes) > len(one_indexes):

            allowed_indexes = zero_indexes

        else:

            allowed_indexes = one_indexes

        if len(allowed_indexes) == 1:

            break

    oxygen = int(input[allowed_indexes[0]], 2)

    return oxygen


def calculate_co2_rating(input):
    """Function to calculate CO2 rating from diagnostic report."""

    n_chars = len(input[0])

    allowed_indexes = [i for i in range(len(input))]

    for char_index in range(n_chars):

        zero_indexes = []
        one_indexes = []

        for allowed_index in allowed_indexes:

            if input[allowed_index][char_index] == "0":

                zero_indexes.append(allowed_index)

            else:

                one_indexes.append(allowed_index)

        if len(zero_indexes) > len(one_indexes):

            allowed_indexes = one_indexes

        else:

            allowed_indexes = zero_indexes

        if len(allowed_indexes) == 1:

            break

    co2 = int(input[allowed_indexes[0]], 2)

    return co2


def calculate_oxygen_and_co2(input):
    """Function to calculate oxygen and CO2 ratings from diagnostic report."""

    oxygen = calculate_oxygen_rating(input)

    co2 = calculate_co2_rating(input)

    return oxygen, co2


if __name__ == "__main__":

    inputs = helpers.load_input("input_1.txt", remove_lines_breaks=True)

    result = calculate_oxygen_and_co2(inputs)

    print(result, result[0] * result[1])
