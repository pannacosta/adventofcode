#day 3 part 1
import string

my_file = open("input_2022_d3.txt", "r")
content = my_file.read()
puzzle_input_d3 = content.strip().split("\n")
my_file.close()

letters = [letter for letter in string.ascii_letters]
priorities = {k:i+1 for i,k in enumerate(letters)}

def select_common_item(sack):
    compartment_size = int(len(sack)/2)
    rucksack_1 = sack[0:compartment_size]
    rucksack_2 = sack[compartment_size:]
    return list(set(rucksack_1).intersection(rucksack_2))[0]

sum([priorities[select_common_item(sacks)] for sacks in puzzle_input_d3])

#day 3 part 2
def select_group_badge(list_of_sacks):
    elf_1,elf_2,elf_3 = list_of_sacks 
    return list(set(elf_1).intersection(elf_2,elf_3))[0]

grouped_elves = [list(puzzle_input_d3[i:i+3]) for i in range(0, len(puzzle_input_d3), 3)]

sum([priorities[select_group_badge(item)] for item in grouped_elves]) 
