#day 5
import itertools
import re
import numpy as np

#whatever I Don't care it assumes there are 9 stacks

my_file = open("input_2022_d5.txt", "r")
content = my_file.read()
puzzle_input_d5 = content.split("\n")
my_file.close()
puzzle_input_d5

cargo,moves = [list(y) for x, y in itertools.groupby(puzzle_input_d5, lambda z: z == '') if not x]
stacks = cargo[-1]

stack_positions = [(num,stacks.index(num)) for num in stacks if num.isnumeric()==True]
stack_numbers = [int(item[0]) for item in stack_positions]
stack_index = [item[1] for item in stack_positions]
pivot_cargo = {int(k):[] for k in stack_numbers}

for stack_level in cargo[:-1]:
    for index, item in enumerate(stack_level):
        if item == ' ':
            pass
        elif index in stack_index:
            pivot_cargo[stack_numbers[stack_index.index(index)]].insert(0,item)

def move_maker(directions,entry_dict):
    num_boxes,start,end = directions
    
    for box in entry_dict[start][-num_boxes:][::-1]:
        entry_dict[end].append(box)
    del entry_dict[start][-num_boxes:]
    
def cratemover_9001(directions,entry_dict):
    num_boxes,start,end = directions
    
    if num_boxes == 1:
        for box in entry_dict[start][-num_boxes:][::-1]:
            entry_dict[end].append(box)
    elif num_boxes > 1:
        for box in entry_dict[start][-num_boxes:]:
            entry_dict[end].append(box)

    del entry_dict[start][-num_boxes:]

moving_directions_as_strings = [re.findall(r'\d+',move) for move in moves]
moving_directions = [[int(item) for item in move] for move in moving_directions_as_strings]

#pt 1 answer
for crane_operation in moving_directions:
    move_maker(crane_operation,pivot_cargo)

''.join([stack[-1] for stack in list(pivot_cargo.values())])

#pt 2 answer
for crane_operation in moving_directions:
    cratemover_9001(crane_operation,pivot_cargo)

''.join([stack[-1] for stack in list(pivot_cargo.values())])
