import puzzle_1


class TestPuzzle1:
    """Tests for puzzle 1."""

    def test_low_point_heights(self, input_1):
        """Test that the heights of low points are correct."""

        assert puzzle_1.find_low_point_heights(input_1) == [1, 0, 5, 5]

    def test_find_risk_level_sum(self, input_1):
        """Test the sum of risk levels are correct."""

        assert puzzle_1.find_risk_level_sum(input_1) == 15


def test_puzzle_2(input_1):

    assert 1 == 1
