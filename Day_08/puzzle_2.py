import puzzle_1


def sum_output_values(input: list[tuple[list[str], ...]]) -> int:
    """Decode all signal wires, find the values of all output numbers
    and return their sum.
    """

    total = 0

    for row in input:

        mapping = find_signal_mapping(row[0])

        output = find_output_digits(row[1], mapping)

        total += output

    return total


def find_signal_mapping(input: list[str]) -> dict:
    """Decode all sign wires to find which wires correspond to which
    digits.
    """

    digit_mapping = {}

    length_five_digits = []
    length_six_digits = []

    # identify the numbers that have unique numbers of segments displayed
    # filter the digits that have 5 and 6 segments
    for signal_wires in input:

        if len(signal_wires) == 2:

            digit_mapping["1"] = signal_wires

        elif len(signal_wires) == 3:

            digit_mapping["7"] = signal_wires

        elif len(signal_wires) == 4:

            digit_mapping["4"] = signal_wires

        elif len(signal_wires) == 7:

            digit_mapping["8"] = signal_wires

        elif len(signal_wires) == 5:

            length_five_digits.append(signal_wires)

        elif len(signal_wires) == 6:

            length_six_digits.append(signal_wires)

    check_dict_has_key(digit_mapping, "1")
    check_dict_has_key(digit_mapping, "7")
    check_dict_has_key(digit_mapping, "4")
    check_dict_has_key(digit_mapping, "8")

    # find digit 6 which only shares 1 segment with digit 1
    for signal_wires in length_six_digits:

        if not all_characters_in_string(digit_mapping["1"], signal_wires):

            digit_mapping["6"] = signal_wires

            length_six_digits.remove(signal_wires)

            break

    check_dict_has_key(digit_mapping, "6")

    # remove segments that digit 4 has in common with digit 1
    digit_4_segments = [char for char in digit_mapping["4"]]

    for digit_1_segment in digit_mapping["1"]:

        digit_4_segments.remove(digit_1_segment)

    if not len(digit_4_segments) == 2:

        raise ValueError("expecting digit_4_segments to have 2 characters")

    digit_4_segments_not_in_1 = "".join(digit_4_segments)

    # find digit 0 for only having 1 segment in common with 4 (excluding the
    # segments shared with digit 1)
    # digit 9 will share both segments
    for signal_wires in length_six_digits:

        if all_characters_in_string(digit_4_segments_not_in_1, signal_wires):

            digit_mapping["9"] = signal_wires

        else:

            digit_mapping["0"] = signal_wires

    check_dict_has_key(digit_mapping, "9")
    check_dict_has_key(digit_mapping, "0")

    # remove segments that digit 8 has in common with digits 7 and 4
    digit_8_segments = [char for char in digit_mapping["8"]]

    for digit_7_segment in digit_mapping["7"]:

        digit_8_segments.remove(digit_7_segment)

    for digit_4_segment in digit_4_segments_not_in_1:

        digit_8_segments.remove(digit_4_segment)

    if not len(digit_8_segments) == 2:

        raise ValueError("expecting digit_8_segments to have 2 characters")

    digit_8_segments_not_in_7_4 = "".join(digit_8_segments)

    # digit 2 shares both the digit 8 segments not in 7, 4
    # digit 5 shares both the digit 4 segments not in 1
    # digit 3 is the remaining digit
    for signal_wires in length_five_digits:

        if all_characters_in_string(digit_8_segments_not_in_7_4, signal_wires):

            digit_mapping["2"] = signal_wires

        elif all_characters_in_string(digit_4_segments_not_in_1, signal_wires):

            digit_mapping["5"] = signal_wires

        else:

            digit_mapping["3"] = signal_wires

    check_dict_has_key(digit_mapping, "2")
    check_dict_has_key(digit_mapping, "3")
    check_dict_has_key(digit_mapping, "5")

    return digit_mapping


def check_dict_has_key(d: dict, key: str) -> None:
    """Check if a dict has a given key and if not raise a KeyError."""

    if key not in d.keys():

        raise KeyError(f"expecting dict to have key {key}")


def all_characters_in_string(characters: str, string: str) -> bool:
    """Find if all characters are present in a string."""

    return all([char in string for char in characters])


def find_output_digits(output: list[str], mapping: dict) -> int:
    """Decode the output digits using a given wire mapping and return
    all digits concatenated together.
    """

    output_digits = ""

    for output_signal in output:

        for mapping_digit, mapping_signal in mapping.items():

            if sort_string(mapping_signal) == sort_string(output_signal):

                output_digits += mapping_digit

                break

    output_digits_int = int(output_digits)

    return output_digits_int


def sort_string(string: str) -> str:
    """Sort a string into alphabetical order."""

    return "".join(sorted(string))


if __name__ == "__main__":

    input = puzzle_1.load_input("input_1.txt")

    result = sum_output_values(input)

    print(result)
