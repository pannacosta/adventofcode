#Challenge 1
#use list comprehension to return true/false read of input
bool_list = [True if puzzle_input[index] > puzzle_input[index-1] else False for index,data in enumerate(puzzle_input)]
print(sum(bool_list))

#Challenge 2
sum_every_3 = [sum(puzzle_input[item:item+3]) for item in range(0,len(puzzle_input))]
bool_list_2 = [True if sum_every_3[index] > sum_every_3[index-1] else False for index,data in enumerate(sum_every_3)]
print(sum(bool_list_2))
