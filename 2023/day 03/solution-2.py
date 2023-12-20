import re
from dataclasses import dataclass
from itertools import product

INPUT_FILE_PATH = "./input.txt"
DIGITS_OR_STAR_PATTERN = r"\d+|\*"
ADJACENT_POSITIONS = [-1, 0, 1]
STAR_PATTERN = "*"

@dataclass(frozen=True)
class Match:
    value: str
    row_index: int
    start_index: int
    end_index: int

def read_input(file_path: str) -> list:
    with open(file_path) as file:
        return [line.strip() for line in file]

def find_matches(line: str, row: int) -> list:
    return [
        Match(item.group(), row, item.start(), item.end())
        for item in re.finditer(DIGITS_OR_STAR_PATTERN, line)
    ]

def has_adjacent_positions(mult: Match, num: Match) -> bool:
    return (
        mult.row_index - num.row_index in ADJACENT_POSITIONS
        and (
            mult.start_index - num.start_index in ADJACENT_POSITIONS
            or mult.end_index - num.end_index in ADJACENT_POSITIONS
        )
    )

def main():
    total_sum = 0
    all_matches = []

    lines = read_input(INPUT_FILE_PATH)

    for row_index, line in enumerate(lines):
        all_matches.extend(find_matches(line, row_index))

    stars = [match for match in all_matches if match.value == STAR_PATTERN]
    nums = [match for match in all_matches if match.value != STAR_PATTERN]

    adjacent_matches = {star: [num for num in nums if has_adjacent_positions(star, num)] for star in stars}

    for star, num in adjacent_matches.items():
        if len(num) > 1:
            total_sum += int(num[0].value) * int(num[1].value)

    print(total_sum)

if __name__ == "__main__":
    main()