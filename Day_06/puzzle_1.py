import sys

sys.path.append("..")
import helpers  # noqa


def load_input(file: str) -> list[int]:
    """Load input file."""

    input = helpers.load_input(file, remove_lines_breaks=True)

    input_processed = [int(x) for x in input[0].split(",")]

    return input_processed


def count_number_of_fish(input: list[int], days: int) -> int:
    """Count the total number of fish after a given number of days and starting
    fish (number of days until they spawn another fish).
    """

    # reset the input to the day each fish spawned with 8 days to go
    # until spawning another fish
    input_reset = [x - 8 for x in input]

    for i, fish in enumerate(input_reset):

        new_fish_spawn_days = get_days_when_fish_spawned(start_day=fish, max_days=days)

        input_reset.extend(new_fish_spawn_days)

    return len(input_reset)


def get_days_when_fish_spawned(start_day: int, max_days: int) -> list[int]:
    """For a single fish return the days (below max_days) on which
    new fish are spawned.

    Parameters
    ----------
    start_day : int
        The index of the day on which the given fish is spawned with
        state 8.

    max_days : int
        The maximum number of days to count up to, finding the days
        on which new fish are spawned.

    """

    spawn_days: list[int] = []

    spawn_day = start_day + 8 + 1

    if spawn_day > max_days:

        return spawn_days

    while spawn_day <= max_days:

        spawn_days.append(spawn_day)

        spawn_day += 6 + 1

    return spawn_days


if __name__ == "__main__":

    input = load_input("input_1.txt")

    result = count_number_of_fish(input, 80)

    print(result)
