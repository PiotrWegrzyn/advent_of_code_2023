import pytest

from day_2.part_1.puzzle import GameValidator, GameRunExtractor


@pytest.mark.parametrize(
    'line, expected',
    [
        ('Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green', [(4, 0, 3), (1, 2, 6), (0, 2, 0)]),
        ('Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue', [(0, 2, 1), (1, 3, 4), (0, 1, 1)]),
        ('Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red', [(20, 8, 6), (4, 13, 5), (1, 5, 0)]),
        ('Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red', [(3, 1, 6), (6, 3, 0), (14, 3, 15)]),
        ('Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green', [(6, 3, 1), (1, 2, 2)]),
    ]
)
def test_extractor(line, expected):
    extractor = GameRunExtractor()
    assert extractor.extract_game(line) == expected


@pytest.mark.parametrize(
    'game_run, expected',
    [
        ([(4, 0, 3), (1, 2, 5), (0, 2, 0)], True),
        ([(0, 2, 1), (1, 3, 4), (0, 1, 1)], True),
        ([(20, 8, 6), (4, 13, 5), (1, 5, 0)], False),
        ([(3, 1, 6), (6, 3, 0), (14, 3, 15)], False),
        ([(6, 3, 1), (1, 2, 2), (0, 0, 0)], True),
    ]
)
def test_validator(game_run, expected):
    validator = GameValidator(12, 13, 14)
    assert validator.validate_game(game_run) == expected

