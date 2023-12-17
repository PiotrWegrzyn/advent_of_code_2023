"""
Day 3: Gear Ratios ---

You and the Elf eventually reach a gondola lift station; he says the gondola lift will take you up to the water source, but this is as far as he can bring you. You go inside.

It doesn't take long to find the gondolas, but there seems to be a problem: they're not moving.

"Aaah!"

You turn around to see a slightly-greasy Elf with a wrench and a look of surprise. "Sorry, I wasn't expecting anyone! The gondola lift isn't working right now; it'll still be a while before I can fix it." You offer to help.

The engineer explains that an engine part seems to be missing from the engine, but nobody can figure out which one. If you can add up all the part numbers in the engine schematic, it should be easy to work out which part is missing.

The engine schematic (your puzzle input) consists of a visual representation of the engine. There are lots of numbers and symbols you don't really understand, but apparently any number adjacent to a symbol, even diagonally, is a "part number" and should be included in your sum. (Periods (.) do not count as a symbol.)

Here is an example engine schematic:

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

In this schematic, two numbers are not part numbers because they are not adjacent to a symbol: 114 (top right) and 58 (middle right). Every other number is adjacent to a symbol and so is a part number; their sum is 4361.

Of course, the actual engine schematic is much larger. What is the sum of all of the part numbers in the engine schematic?
"""
import re


class EngineMap:
    def __init__(self, text_input: list[str]):
        self.map = text_input

    def get_engine_part_numbers(self) -> list[int]:
        numbers = []
        for y in range(len(engine_map.map)):
            skip_stack = 0
            for x in range(len(engine_map.map[y])):
                if skip_stack > 0:
                    skip_stack -= 1
                    continue
                if engine_map.map[y][x].isdigit():
                    number_len = self.get_len_of_number(x, y)
                    skip_stack = number_len - 1
                    neighbours = self.get_neighbours(x, y, digits=number_len)
                    if self.contains_symbol(neighbours):
                        numbers.append(self.build_number(x, y, number_len))

        return numbers

    def get_neighbours(self, x: int, y: int, digits=1) -> str:
        x_start = max(0, x - 1)
        x_stop = min(len(self.map)-1, x + 1 + digits - 1)
        y_start = max(0, y - 1)
        y_stop = min(len(self.map[0])-1, y + 1)

        neighbours = ''
        if y-1 >= 0:
            neighbours += self.map[y_start][x_start:x_stop+1]

        neighbours += self.map[y][x_start] + self.map[y][x_stop]

        if y+1 < len(self.map):
            neighbours += self.map[y_stop][x_start:x_stop+1]

        return neighbours

    def get_len_of_number(self, x, y) -> int:
        digits = 1
        while x+1 < len(self.map[y]) and self.map[y][x+1].isdigit():
            x += 1
            digits += 1
        return digits

    def contains_symbol(self, neighbours: str) -> bool:
        return bool(re.findall(r'([^.\d])', neighbours))

    def build_number(self, x, y, number_len) -> int:
        return int(self.map[y][x:x+number_len])


if __name__ == '__main__':
    puzzle_input = open('../puzzle_input.txt').read().splitlines()
    engine_map = EngineMap(puzzle_input)
    engine_part_numbers = engine_map.get_engine_part_numbers()
    print(sum(engine_part_numbers))
