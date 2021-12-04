#Day 3
#challenge 1
import pandas as pd

my_file = open("C:/Users/pauls/Desktop/input_d3.txt", "r")
content = my_file.read()
puzzle_input_d3 = content.split("\n")
my_file.close()

puzzle_input_d3_tups = [tuple(digit for digit in number) for number in puzzle_input_d3]

gamma_rate_as_list = pd.DataFrame(puzzle_input_d3_tups).mode().values.tolist()[0]
gamma_rate_bin = ''.join(gamma_rate_as_list)
gamma_rate = int(gamma_rate_bin,2)

swap = {0:'1', 1:'0'}
epsilon_rate_as_list = [swap[int(value)] for value in gamma_rate_as_list]
epsilon_rate_bin = ''.join(epsilon_rate_as_list)
epsilon_rate = int(epsilon_rate_bin,2)

print(epsilon_rate*gamma_rate)
