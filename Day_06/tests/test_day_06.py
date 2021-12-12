import puzzle_1

import pytest


class TestPuzzle1:
    @pytest.mark.parametrize(
        "start_day,max_days,expected_counts", [(2, 18, [11, 18]), (-4, 5, [5])]
    )
    def test_get_days_when_fish_spawned(self, start_day, max_days, expected_counts):

        assert (
            puzzle_1.get_days_when_fish_spawned(start_day, max_days) == expected_counts
        )

    @pytest.mark.parametrize(
        "n_days,expected_counts", [(18, 26), (80, 5934), (256, 26984457539)]
    )
    def test_count_number_of_fish(self, input_1, n_days, expected_counts):

        assert puzzle_1.count_number_of_fish(input_1, n_days) == expected_counts


class TestPuzzle2:
    @pytest.mark.parametrize("n_days,expected_counts", [(256, 26984457539)])
    def test_count_number_of_fish(self, input_1, n_days, expected_counts):

        assert puzzle_1.count_number_of_fish(input_1, n_days) == expected_counts
