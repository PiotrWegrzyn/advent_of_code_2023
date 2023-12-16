"""
Your puzzle answer was 54605.

The first half of this puzzle is complete! It provides one gold star: *
--- Part Two ---

Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters: one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".

Equipped with this new information, you now need to find the real first and last digit on each line. For example:

two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen

In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.

What is the sum of all of the calibration values?

Answer:

Although it hasn't changed, you can still get your puzzle input.

You can also [Shareon Twitter Mastodon] this puzzle.
"""



if __name__ == '__main__':
    input_lines = open('calibration_input.txt').read().splitlines()
    print(get_sum_calibration_values(input_lines))
