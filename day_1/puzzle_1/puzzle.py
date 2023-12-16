"""
The newly-improved calibration document consists of lines of text;
Each line originally contained a specific calibration value that the Elves now need to recover.
On each line, the calibration value can be found by combining the first digit and the last digit
(in that order) to form a single two-digit number.

For example:
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet

In this example, the calibration values of these four lines are 12, 38, 15, and 77.
Adding these together produces 142.

Consider your entire calibration document. What is the sum of all of the calibration values?
"""


class CalibrationSumExtractor:
    def __init__(self, lines: list[str]):
        self.lines = lines

    def get_sum(self) -> int:
        return sum(self._get_calibration_value(self._extract_digits(line)) for line in self.lines)

    def _extract_digits(self, line: str) -> list[int]:
        return [int(s) for s in line if s.isdigit()]

    def _get_calibration_value(self, digits: list[int]) -> int:
        return digits[0] * 10 + digits[-1]


if __name__ == '__main__':
    input_lines = open('calibration_input.txt').read().splitlines()
    extractor = CalibrationSumExtractor(input_lines)
    print(extractor.get_sum())
