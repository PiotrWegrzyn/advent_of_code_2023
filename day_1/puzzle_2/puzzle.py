"""
Your puzzle answer was 54605.

The first half of this puzzle is complete! It provides one gold star: *
--- Part Two ---

Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters: one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".

Equipped with this new information, you now need to find the real first and last digit on each line. For example:

two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen

In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.

What is the sum of all of the calibration values?

Answer:

Although it hasn't changed, you can still get your puzzle input.

You can also [Shareon Twitter Mastodon] this puzzle.
"""
from typing import Optional

from day_1.puzzle_1.puzzle import CalibrationSumExtractor


class CalibrationSumWordExtractor(CalibrationSumExtractor):
    spelled_digits = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    def _extract_digits(self, line: str) -> list[int]:
        digits = []
        for offset, char in enumerate(line):
            if char.isdigit():
                digits.append(int(char))
            else:
                spelled_digit = self._extract_spelled_digit(line, offset)
                if spelled_digit is not None:
                    digits.append(spelled_digit)

        return digits

    def _extract_spelled_digit(self, line: str, offset: int) -> Optional[int]:
        for digit, spelled_digit in enumerate(self.spelled_digits):
            if line[offset:].startswith(spelled_digit):
                return digit

        return None


if __name__ == '__main__':
    input_lines = open('../calibration_input.txt').read().splitlines()
    extractor = CalibrationSumWordExtractor(input_lines)
    print(extractor.get_sum())