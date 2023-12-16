import pytest

from day_2.part_2.puzzle import GameRequirements


@pytest.mark.parametrize(
    'game_run, expected',
    [
        ([(4, 0, 3), (1, 2, 5), (0, 2, 0)], (4, 2, 5)),
        ([(20, 8, 6), (4, 13, 5), (1, 5, 0)], (20, 13, 6)),
    ]
)
def test_minimum_games(game_run, expected):
    validator = GameRequirements()
    assert validator.get_min(game_run) == expected
