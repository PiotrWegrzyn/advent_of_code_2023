import pytest

from day_3.part_1.puzzle import EngineMap


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
    return EngineMap(example_map)


@pytest.mark.parametrize(
    'x,y, digits, expected', [
        (0, 0, 1, [['', '', ''], ['', '4', '6'], ['', '.', '.']]),
        (0, 0, 2, [['', '', '', ''], ['', '4', '6', '7'], ['', '.', '.', '.']]),
        (2, 2, 2, [['.', '.', '*', '.'], ['.', '3', '5', '.'], ['.', '.', '.', '.']]),
        (2, 2, 1, [['.', '.', '*'], ['.', '3', '5'], ['.', '.', '.']]),
        (9, 9, 1, [['.', '.', ''], ['.', '.', ''], ['', '', '']]),
    ]
)
def test_get_neighbours(x, y, digits, expected, example_map):
    assert example_map.get_neighbours(x, y, digits) == expected


@pytest.mark.parametrize(
    'x,y, digits, expected', [
        (0, 0, 1, 4),
        (0, 0, 3, 467),
        (2, 2, 2, 35),
    ]
)
def test_build_number(x, y, digits, expected, example_map):
    assert example_map.build_number(x, y, digits) == expected


@pytest.mark.parametrize(
    'x,y, expected', [
        (0, 0, 3),
        (2, 2, 2),
        (7, 5, 2),
        (6, 7, 4),
    ]
)
def test_get_len(x, y, expected, example_map):
    assert example_map.get_len_of_number(x, y) == expected


@pytest.mark.parametrize(
    'neighbours, expected', [
        ([['', '', '', ''], ['', '4', '6', '7'], ['', '.', '.', '.']], False),
        ([['.', '.', '*'], ['.', '3', '5'], ['.', '.', '.']], True),

    ]
)
def test_contains_symbol(neighbours, expected, example_map):
    assert example_map.contains_symbol(neighbours) == expected
