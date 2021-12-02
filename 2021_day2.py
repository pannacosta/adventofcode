#challenge 1
import pandas as pd

my_file = open("filepath/input.txt", "r")
content = my_file.read()
puzzle_input_d2 = content.split("\n")
my_file.close()

list_o_tuples = [tuple(item.split(" ")) for item in puzzle_input_d2 if len(item)>0]

for index, item in enumerate(list_o_tuples):
    position, value = item
    if list_o_tuples[index][0] == 'up':
        list_o_tuples[index] = (position, -int(value))
    else:
        list_o_tuples[index] = (position, int(value))

data_df = pd.DataFrame(list_o_tuples,columns = ['position','value']).groupby('position',as_index=False).sum()

horizontal = data_df['value'].loc[data_df['position'] == 'forward'].values[0]
depth = data_df.loc[data_df['position'].isin(['up','down']), 'value'].sum()
print(horizontal*depth)

#challenge 2
import pandas as pd

my_file = open("filepath/input.txt", "r")
content = my_file.read()
puzzle_input_d2 = content.split("\n")
my_file.close()

list_o_tuples = [tuple(item.split(" ")) for item in puzzle_input_d2 if len(item)>0]

for index, item in enumerate(list_o_tuples):
    position, value = item
    if list_o_tuples[index][0] == 'up':
        position = 'direction'
        list_o_tuples[index] = (position, -int(value))
    elif list_o_tuples[index][0] == 'down':
        position = 'direction'
        list_o_tuples[index] = (position, int(value))
    else:
        list_o_tuples[index] = (position, int(value))

aim = 0
horizontal_total = 0
depth = 0

for index, item in enumerate(list_o_tuples):
    if list_o_tuples[index][0] == 'direction':
        aim += list_o_tuples[index][1]
    if list_o_tuples[index][0] == 'forward':
        horizontal_current = list_o_tuples[index][1]
        horizontal_total += list_o_tuples[index][1]
        depth_change = aim*horizontal_current
        depth += depth_change

print(horizontal_total*depth)  
