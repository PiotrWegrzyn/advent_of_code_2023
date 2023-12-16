import pytest

from day_1.part_1.puzzle import CalibrationSumExtractor


@pytest.mark.parametrize(
    'line, expected',
    [
        ('1abc2', [1, 2]),
        ('pqr3stu8vwx', [3, 8]),
        ('a1b2c3d4e5f', [1, 2, 3, 4, 5]),
        ('treb7uchet', [7]),
    ]
)
def test_extract_digits(line, expected):
    extractor = CalibrationSumExtractor([line])
    assert extractor._extract_digits(line) == expected


@pytest.mark.parametrize(
    'line, expected',
    [
        ([1, 5], 15),
        ([7], 77),
    ]
)
def test_get_calibration_value(line, expected):
    extractor = CalibrationSumExtractor([])
    assert extractor._get_calibration_value(line) == expected


def test_calibration_sum_extractor():
    lines = [
        '1abc2',
        'pqr3stu8vwx',
        'a1b2c3d4e5f',
        'treb7uchet',
    ]
    extractor = CalibrationSumExtractor(lines)
    assert extractor.get_sum() == 142
