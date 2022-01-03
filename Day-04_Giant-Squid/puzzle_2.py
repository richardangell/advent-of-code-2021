import numpy as np
from numpy.typing import ArrayLike
import sys
from puzzle_1 import load_input

sys.path.append("..")
import helpers  # noqa


def calculate_last_winning_score(
    draw_numbers: list[int], boards: list[ArrayLike], blank_boards: list[ArrayLike]
) -> tuple[int, int, int]:
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
