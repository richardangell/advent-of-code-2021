import puzzle_1


if __name__ == "__main__":

    input = puzzle_1.load_input("input_1.txt")

    result = puzzle_1.count_number_of_fish(input, 256)

    print(result)
