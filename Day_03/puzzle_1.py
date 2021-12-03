import sys

sys.path.append("..")
import helpers  # noqa


def calculate_gamma_and_epsilon(input):
    """Function to calculate gamma and epsilon from diagnostic report."""

    n_chars = len(input[0])

    gamma_binary = ""
    epsilon_binary = ""

    for char_index in range(n_chars):

        zero_count = 0
        one_count = 0

        for row in input:

            if row[char_index] == "0":

                zero_count += 1

            else:

                one_count += 1

        if zero_count > one_count:

            gamma_binary += "0"
            epsilon_binary += "1"

        else:

            gamma_binary += "1"
            epsilon_binary += "0"

    gamma = int(gamma_binary, 2)
    epsilon = int(epsilon_binary, 2)

    return gamma, epsilon


if __name__ == "__main__":

    inputs = helpers.load_input("input_1.txt", remove_lines_breaks=True)

    result = calculate_gamma_and_epsilon(inputs)

    print(result, result[0] * result[1])
