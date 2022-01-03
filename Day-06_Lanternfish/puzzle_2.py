from collections import Counter

import puzzle_1


def count_number_of_fish_unique(input: list[int], days: int) -> int:
    """Count the total number of fish after a given number of days and starting
    fish (number of days until they spawn another fish).

    The difference from the solution to puzzle 1 is that counts of starting
    values are created so that each unique starting value only has to be
    iterated from once.

    """

    input_counts = Counter(input)

    total_counts = 0

    for start_day, day_count in input_counts.items():

        start_day_counts = puzzle_1.count_number_of_fish(input=[start_day], days=days)

        total_counts += start_day_counts * day_count

    return total_counts


def count_number_of_fish(input: list[int], days: int) -> int:
    """Count the total number of fish after a given number of days and starting
    fish (number of days until they spawn another fish).
    """

    # reset the input to the day each fish spawned with 8 days to go
    # until spawning another fish
    input_reset = [x - 8 for x in input]

    # for each value in the input count the number of times it appears
    input_counts = Counter(input_reset)

    spawn_day_counts = get_spawn_day_counts(input, days)

    # include the starting fish at time 0
    total_counts = len(input)

    for day, day_count in input_counts.items():

        total_counts += spawn_day_counts[day] * day_count

    return total_counts


def get_spawn_day_counts(input: list[int], days: int) -> dict[int, int]:
    """Count the total number of fish after a given number of days and starting
    fish (number of days until they spawn another fish).
    """

    spawn_day_counter: dict[int, int] = {}

    for spawn_day in range(days, -9, -1):

        # get the days this fish will spawn new fish
        subsequent_spawn_days = puzzle_1.get_days_when_fish_spawned(
            start_day=spawn_day, max_days=days
        )

        spawn_day_count = len(subsequent_spawn_days)

        count_subsequent_spawn_days = Counter(subsequent_spawn_days)

        for (
            earlier_spawn_day,
            earlier_spawn_day_count,
        ) in count_subsequent_spawn_days.items():

            spawned_fish_of_spawned_fish = (
                spawn_day_counter[earlier_spawn_day] * earlier_spawn_day_count
            )

            spawn_day_count += spawned_fish_of_spawned_fish

        spawn_day_counter[spawn_day] = spawn_day_count

    return spawn_day_counter


if __name__ == "__main__":

    input = puzzle_1.load_input("input_1.txt")

    result = count_number_of_fish(input, 256)

    print(result)
