"""
--- Day 1: Trebuchet?! ---

Something is wrong with global snow production, and you've been selected to take a look. The Elves have even given you a map; on it, they've used stars to mark the top fifty locations that are likely to be having problems.

You've been doing this long enough to know that to restore snow operations, you need to check all fifty stars by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

You try to ask why they can't just use a weather machine ("not powerful enough") and where they're even sending you ("the sky") and why your map looks mostly blank ("you sure ask a lot of questions") and hang on did you just say the sky ("of course, where do you think snow comes from") when you realize that the Elves are already loading you into a trebuchet ("please hold still, we need to strap you in").

As they're making the final adjustments, they discover that their calibration document (your puzzle input) has been amended by a very young Elf who was apparently just excited to show off her art skills. Consequently, the Elves are having trouble reading the values on the document.

The newly-improved calibration document consists of lines of text; each line originally contained a specific calibration value that the Elves now need to recover. On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.

For example:

1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet

In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.

Consider your entire calibration document. What is the sum of all of the calibration values?
"""


class CalibrationSumExtractor:
    def __init__(self, lines: list[str]):
        self.lines = lines

    def get_sum(self) -> int:
        return sum(self._get_calibration_value(self._extract_digits(line)) for line in self.lines)

    @staticmethod
    def _extract_digits(line: str) -> list[int]:
        return [int(s) for s in line if s.isdigit()]

    @staticmethod
    def _get_calibration_value(digits: list[int]) -> int:
        return digits[0] * 10 + digits[-1]


if __name__ == '__main__':
    input_lines = open('../calibration_input.txt').read().splitlines()
    extractor = CalibrationSumExtractor(input_lines)
    print(extractor.get_sum())
