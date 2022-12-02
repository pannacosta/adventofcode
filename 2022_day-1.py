import re
import pandas as pd

my_file = open("input_2022_d1.txt", "r")
content = my_file.read()
puzzle_input_d1 = content.split("\n\n")
my_file.close()

for index, item in enumerate(puzzle_input_d1):
    puzzle_input_d1[index] = item.split("\n")

for index, item in enumerate(puzzle_input_d1):
    puzzle_input_d1[index] = sum([int(value) for value in item if value != ''])
    
max_value = max(puzzle_input_d1)
max_index = puzzle_input_d1.index(max_value)

# pt 1 answer
max_value
# pt 2 answer
sum(sorted(puzzle_input_d1, reverse=True)[:3])
