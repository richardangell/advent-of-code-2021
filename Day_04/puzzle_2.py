import numpy as np
import sys

sys.path.append("..")
import helpers  # noqa


def load_input(file):
    """Functiont to load the input file and return the numbers, boards with
    numbers and blank boards.
    """

    input = helpers.load_input(file, remove_lines_breaks=True)

    draw_numbers = [int(x) for x in input[0].split(",")]

    boards = []

    next_board = []

    for i, row in enumerate(input[2:]):

        if row == "":

            pass

        else:

            row_split = row.split(" ")

            row_split = [int(x) for x in row_split if x != ""]

            next_board.append(row_split)

            if len(next_board) == 5:

                boards.append(np.array(next_board))

                next_board = []

    blank_board = np.array([[0, 0, 0, 0, 0]] * 5)

    blank_boards = [blank_board] * len(boards)

    return draw_numbers, boards, blank_boards


def calculate_last_winning_score(draw_numbers, boards, blank_boards):
    """Function to calculate the winning score from the
    board which would win last. The score is given by
    sum of all unmarked numbers on that board multiplied
    by the number that was just called for the winning
    board.
    """

    boards_in_play = [i for i in range(len(boards))]

    remove_board = []

    for drawn_number in draw_numbers:

        for board_no in boards_in_play:

            board = boards[board_no]
            blank_board = blank_boards[board_no]

            drawn_number_found = board == drawn_number

            if drawn_number_found.sum() > 0:

                blank_board = blank_board + drawn_number_found

                blank_board = np.clip(blank_board, a_min=None, a_max=1)

                blank_boards[board_no] = blank_board

                unmarked_board = (1 - blank_board) * board

                # check for winning board
                if (blank_board.sum(axis=0) == 5).any() or (
                    blank_board.sum(axis=1) == 5
                ).any():

                    # if the board wins, store the board number and remove it
                    # outside of the loop
                    if len(boards_in_play) > 1:

                        remove_board.append(board_no)

                    else:

                        unmarked_board = (1 - blank_board) * board

                        unmarked_board_score = unmarked_board.sum()

                        return (
                            unmarked_board_score * drawn_number,
                            unmarked_board_score,
                            drawn_number,
                        )

        if remove_board is not []:

            for board_to_remove in remove_board:

                boards_in_play.remove(board_to_remove)

            remove_board = []


if __name__ == "__main__":

    input = load_input("input_1.txt")

    result = calculate_last_winning_score(*input)

    print(result)
