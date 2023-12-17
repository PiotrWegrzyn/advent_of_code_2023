"""
--- Part Two ---

The engineer finds the missing part and installs it in the engine! As the engine springs to life, you jump in the closest gondola, finally ready to ascend to the water source.

You don't seem to be going very fast, though. Maybe something is still wrong? Fortunately, the gondola has a phone labeled "help", so you pick it up and the engineer answers.

Before you can explain the situation, she suggests that you look out the window. There stands the engineer, holding a phone in one hand and waving with the other. You're going so slowly that you haven't even left the station. You exit the gondola.

The missing part wasn't the only issue - one of the gears in the engine is wrong. A gear is any * symbol that is adjacent to exactly two part numbers. Its gear ratio is the result of multiplying those two numbers together.

This time, you need to find the gear ratio of every gear and add them all up so that the engineer can figure out which gear needs to be replaced.

Consider the same engine schematic again:

467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..

In this schematic, there are two gears. The first is in the top left; it has part numbers 467 and 35, so its gear ratio is 16345. The second gear is in the lower right; its gear ratio is 451490. (The * adjacent to 617 is not a gear because it is only adjacent to one part number.) Adding up all of the gear ratios produces 467835.

What is the sum of all of the gear ratios in your engine schematic?
"""
from day_3.part_1.puzzle import EngineMap


class GearEngineMap(EngineMap):
    def get_gear_ratios(self) -> list[int]:
        gear_ratios = []
        for y in range(len(self.map)):
            for x in range(len(self.map[y])):
                if self.map[y][x] == '*':
                    gear_ratios.append(self.get_gear_ratio(x, y))

        return gear_ratios

    def get_gear_ratio(self, x, y) -> int:
        # todo fix to make it testable
        engine_part_numbers = []
        neighbours = self.get_neighbours(x, y)

        mid_digits = self.get_digit_positions(neighbours[1])
        if 0 in mid_digits:
            x_begin = self.find_beginning_of_number(x-1, y)
            engine_part_numbers.append(self.get_part_value(x_begin, y))

        if 2 in mid_digits:
            engine_part_numbers.append(self.get_part_value(x+1, y))

        top_digits = self.get_digit_positions(neighbours[0])
        if top_digits:
            if top_digits == [0, 2]:
                x_begin = self.find_beginning_of_number(x-1, y-1)
                engine_part_numbers.append(self.get_part_value(x_begin, y-1))
                engine_part_numbers.append(self.get_part_value(x+1, y-1))
            else:
                x_begin = self.find_beginning_of_number(x-1+top_digits[0], y-1)
                engine_part_numbers.append(self.get_part_value(x_begin, y-1))

        bottom_digits = self.get_digit_positions(neighbours[2])
        if bottom_digits:
            if bottom_digits == [0, 2]:
                x_begin = self.find_beginning_of_number(x-1, y+1)
                engine_part_numbers.append(self.get_part_value(x_begin, y+1))
                engine_part_numbers.append(self.get_part_value(x+1, y+1))
            else:
                x_begin = self.find_beginning_of_number(x-1+bottom_digits[0], y+1)
                engine_part_numbers.append(self.get_part_value(x_begin, y+1))

        if len(engine_part_numbers) == 2:
            return engine_part_numbers[0] * engine_part_numbers[1]
        else:
            return 0

    def get_part_value(self, x, y) -> int:
        number_len = self.get_len_of_number(x, y)
        return self.build_number(x, y, number_len)

    def find_beginning_of_number(self, x, y):
        while x-1 >= 0 and self.map[y][x-1].isdigit():
            x -= 1

        return x

    @staticmethod
    def get_digit_positions(row: list[str]) -> list[int]:
        return [i for i, char in enumerate(row) if char.isdigit()]


if __name__ == '__main__':
    puzzle_input = open('../puzzle_input.txt').read().splitlines()
    engine_map = GearEngineMap(puzzle_input)
    gear_ratios = engine_map.get_gear_ratios()
    print(sum(gear_ratios))
