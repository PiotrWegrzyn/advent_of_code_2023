import pytest

from day_1.part_2.puzzle import CalibrationSumWordExtractor


@pytest.mark.parametrize(
    'line, expected',
    [
        ('two1nine', [2, 1, 9]),
        ('eightwothree', [8, 2, 3]),
        ('abcone2threexyz', [1, 2, 3]),
        ('xtwone3four', [2, 1, 3, 4]),
        ('4nineeightseven2', [4, 9, 8, 7, 2]),
        ('zoneight234', [1, 8, 2, 3, 4]),
        ('7pqrstsixteen', [7, 6]),
    ]
)
def test_extract_digits(line, expected):
    extractor = CalibrationSumWordExtractor([line])
    assert extractor._extract_digits(line) == expected


def test_calibration_sum_extractor():
    lines = [
        'two1nine',
        'eightwothree',
        'abcone2threexyz',
        'xtwone3four',
        '4nineeightseven2',
        'zoneight234',
        '7pqrstsixteen',
    ]
    extractor = CalibrationSumWordExtractor(lines)
    assert extractor.get_sum() == 281
