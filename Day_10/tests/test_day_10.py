import puzzle_1
import puzzle_2

import pytest


class TestPuzzle1:
    """Tests for puzzle 1."""

    @pytest.mark.parametrize(
        "chunk,illegal_char",
        [
            ("[({(<(())[]>[[{[]{<()<>>", None),
            ("[(()[<>])]({[<{<<[]>>(", None),
            ("{([(<{}[<>[]}>{[]{[(<()>", "}"),
            ("(((({<>}<{<{<>}{[]{[]{}", None),
            ("[[<[([]))<([[{}[[()]]]", ")"),
            ("[{[{({}]{}}([{[{{{}}([]", "]"),
            ("{<[[]]>}<{[{[{[]{()[[[]", None),
            ("[<(<(<(<{}))><([]([]()", ")"),
            ("<{([([[(<>()){}]>(<<{{", ">"),
            ("<{([{{}}[<[[[<>{}]]]>[]]", None),
        ],
    )
    def test_find_error_character(self, chunk, illegal_char):
        """Test find_error_character finds the correct illegal character."""

        assert puzzle_1.find_error_character(chunk) == illegal_char

    def test_find_syntax_error_score(self, input_1):
        """Test find_syntax_error_score correct."""

        assert puzzle_1.find_syntax_error_score(input_1) == 26397


class TestPuzzle2:
    """Tests for puzzle 2."""

    @pytest.mark.parametrize(
        "chunk,expected",
        [
            ("[({(<(())[]>[[{[]{<()<>>", "}}]])})]"),
            ("[(()[<>])]({[<{<<[]>>(", ")}>]})"),
            ("(((({<>}<{<{<>}{[]{[]{}", "}}>}>))))"),
            ("{<[[]]>}<{[{[{[]{()[[[]", "]]}}]}]}>"),
            ("<{([{{}}[<[[[<>{}]]]>[]]", "])}>"),
        ],
    )
    def test_find_closing_characters(self, chunk, expected):
        """Test find_closing_characters produces the correct output."""

        assert puzzle_2.find_closing_characters(chunk) == expected

    @pytest.mark.parametrize(
        "chars,expected",
        [
            ("}}]])})]", 288957),
            (")}>]})", 5566),
            ("}}>}>))))", 1480781),
            ("]]}}]}]}>", 995444),
            ("])}>", 294),
        ],
    )
    def test_score_closing_characters(self, chars, expected):
        """Test score_closing_characters produces the correct output."""

        assert puzzle_2.score_closing_characters(chars) == expected

    def test_find_middle_autocomplete_score(self, input_1):
        """Test find_middle_autocomplete_score gives the correct output."""

        assert puzzle_2.find_middle_autocomplete_score(input_1) == 288957
