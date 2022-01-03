import numpy as np
from heapq import heappush, heappop
from collections import defaultdict
from numpy.typing import ArrayLike
import sys

sys.path.append("..")
import helpers  # noqa


RIGHT = (1, 0)
DOWN = (0, 1)
LEFT = (-1, 0)
UP = (0, -1)

START = (0, 0)

DIRECTIONS = [RIGHT, DOWN, UP, LEFT]
DIRECTIONS_REVERSED = [direction for direction in reversed(DIRECTIONS)]


def load_input(file: str) -> ArrayLike:
    """Load the input file and return np.Array of risk scores for the cave."""

    rows = helpers.load_input(file, remove_lines_breaks=True)

    return np.array([[int(value) for value in row] for row in rows])


def find_lowest_risk_score(cave: ArrayLike) -> int:
    """Find the lowest risk score of all paths through the cave."""

    end_coord = (cave.shape[1] - 1, cave.shape[0] - 1)

    results = a_star((0, 0), end_coord, cave)

    return results


def a_star(
    start_node: tuple[int, int], end_node: tuple[int, int], cave: ArrayLike
) -> int:
    """A* algorithm to find the shortest path between two nodes on a graph."""

    def heuristic(node: tuple[int, int], end_node: tuple[int, int] = end_node) -> int:
        """Heuristic function to estimate the cost from the current node
        to the end node.

        Note, must underestimate the cost and never overestimate.

        For this heuristic, estimate that the cost to travel between each
        node until the end is 1.

        """

        return (end_node[0] - node[0]) + (end_node[1] - node[1])

    # use heappush and heappush with open_list to make it a heap queue
    open_list: list = []
    heappush(open_list, (0, start_node))

    # dict to record the previous node to the current in the path to end
    came_from = {}

    # dict to hold the cost of the path from start node to the current node
    g_score: defaultdict = defaultdict(lambda: float("inf"))
    g_score[start_node] = 0

    while len(open_list) > 0:

        _, current_node = heappop(open_list)

        if current_node == end_node:

            return g_score[end_node]

        for next_direction in DIRECTIONS:

            neighbour = add_coords(current_node, next_direction)

            if within_limits(cave, neighbour):

                tentative_g_score = (
                    g_score[current_node] + cave[neighbour[1], neighbour[0]]
                )

                if tentative_g_score < g_score[neighbour]:

                    came_from[neighbour] = current_node
                    g_score[neighbour] = tentative_g_score
                    f_score_neighbour = tentative_g_score + heuristic(current_node)
                    heappush(open_list, (f_score_neighbour, neighbour))

    raise ValueError("end node never reached but open_list is empty")


def reconstruct_path(came_from, current_node):
    """Reconstruct the path from the end node back to the beginning using the
    mapping of previous nodes.
    """

    total_path = [current_node]

    while current_node in came_from.keys():

        current_node = came_from[current_node]

        total_path.insert(0, current_node)

    return total_path


def add_coords(coord1: tuple[int, int], coord2: tuple[int, int]) -> tuple[int, int]:
    """Add two coordinates together."""

    return coord1[0] + coord2[0], coord1[1] + coord2[1]


def within_limits(cave: ArrayLike, coord: tuple[int, int]) -> bool:
    """Check whether a given coordinate is within the limits of the cave."""

    return (
        (0 <= coord[0])
        & (coord[0] <= cave.shape[1] - 1)
        & (0 <= coord[1])
        & (coord[1] <= cave.shape[0] - 1)
    )


if __name__ == "__main__":

    input = load_input("input_1.txt")

    result = find_lowest_risk_score(input)

    print(result)
