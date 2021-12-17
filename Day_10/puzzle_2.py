import puzzle_1


def find_closing_characters(chunk: str) -> str:
    """Return the closing characters that complete an incomplete chunk."""

    stack = []

    bracket_mapping = {")": "(", "]": "[", "}": "{", ">": "<"}

    bracket_mapping_reversed = {v: k for k, v in bracket_mapping.items()}

    open_brackets = ["(", "[", "{", "<"]

    for char in chunk:

        if char in open_brackets:

            stack.append(char)

        else:

            top_char = stack.pop()

            if top_char != bracket_mapping[char]:

                raise ValueError("unexoected illegal character in ")

    closing_characters = [bracket_mapping_reversed[char] for char in stack]

    return "".join([x for x in reversed(closing_characters)])


def score_closing_characters(closing_characters: str) -> int:
    """Calculate the autocomplete score for a set of closing characters."""

    closing_char_mapping = {")": 1, "]": 2, "}": 3, ">": 4}

    autocomplete_score = 0

    for char in closing_characters:

        autocomplete_score *= 5

        autocomplete_score += closing_char_mapping[char]

    return autocomplete_score


def find_middle_autocomplete_score(input: list[str]) -> int:
    """Find the middle autocomplete score for the incomplete lines
    in the input.
    """

    autocomplete_scores: list[int] = []

    for chunk in input:

        illegal_character = puzzle_1.find_error_character(chunk)

        if illegal_character is None:

            closing_characters = find_closing_characters(chunk)

            closing_characters_score = score_closing_characters(closing_characters)

            autocomplete_scores.append(closing_characters_score)

    autocomplete_scores = sorted(autocomplete_scores)

    return autocomplete_scores[int(len(autocomplete_scores) / 2)]


if __name__ == "__main__":

    input = puzzle_1.load_input("input_1.txt")

    result = find_middle_autocomplete_score(input)

    print(result)
