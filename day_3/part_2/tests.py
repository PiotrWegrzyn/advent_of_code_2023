import pytest

from day_3.part_2.puzzle import GearEngineMap


@pytest.fixture
def example_map():
    example_map = [
        '467..114..',
        '...*......',
        '..35..633.',
        '......#...',
        '617*......',
        '.....+.58.',
        '..592.....',
        '......7558',
        '...$.*....',
        '.664.598..',
    ]
    return GearEngineMap(example_map)


@pytest.mark.parametrize(
    'text, expected', [
        ('467', [0, 1, 2]),
        ('6&7', [0, 2]),
        ('...', []),
        ('.*.', []),
        ('.*1', [2]),
        ('1.1', [0, 2]),
        (['1', '', '2'], [0, 2]),
    ]
)
def test_get_digit_positions(text, expected, example_map):
    assert example_map.get_digit_positions(text) == expected


@pytest.mark.parametrize(
    'x,y, expected', [
        (0, 0, 467),
        (2, 2, 35),
        (7, 5, 58),
        (6, 7, 7558),
    ]
)
def test_get_part_value(x, y, expected, example_map):
    assert example_map.get_part_value(x, y) == expected


@pytest.mark.parametrize(
    'x,y, expected', [
        (2, 0, 0),
        (2, 2, 2),
        (8, 5, 7),
        (9, 7, 6),
    ]
)
def test_find_beginning_of_number(x, y, expected, example_map):
    assert example_map.find_beginning_of_number(x, y) == expected


def test_get_gear_ratios(example_map):
    example_map.map = [
        '467..114..',
        '...*......',
        '..35..633.',
        '......#...',
        '617*......',
        '.....+.58.',
        '..592.....',
        '......755.',
        '...$.*....',
        '.664.598..',
    ]

    assert example_map.get_gear_ratios() == [16345, 0, 451490]
    assert sum(example_map.get_gear_ratios()) == 467835
