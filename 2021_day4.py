import re
import numpy as np

my_file = open("somefilepath.txt", "r")
read_file = my_file.read()
my_file.close()

#clean the input
content = [x.split(',') for x in read_file.split('\n\n')]
bingo_list,cards = [int(x) for x in ans[0]],[re.split(r"\s+",card[0].strip()) for card in ans[1:]]
cards = [[int(string) for string in card] for card in cards]
matrix_dimensions = 5

def horizontal_check(score_card):
    #take every group of (dimension) numbers - is len(5) of any group? Return that group
    sectioned_list = np.array_split(score_card, matrix_dimensions)
    check = [x for x in sectioned_list if np.count_nonzero(x) == 5]
    if len(check) == 1:
        return check[0]
    else:
        return False

def vertical_check(score_card):
    #change list into list of lists of every N elements
    sectioned_list = [score_card[index::matrix_dimensions] for index,number in enumerate(score_card) if index <= matrix_dimensions]
    check = [x for x in sectioned_list if np.count_nonzero(x) == 5]
    if len(check) == 1:
        return check[0]
    else:
        return False

#didn't need this but I liked my logic so I left it in
def diagonal_check(score_card):
    #turn into list of lists by matrix rows
    sectioned_list = np.array_split(score_card, matrix_dimensions)
    #use diag calculation in for loop
    diag_rows = [[],[]]
    for row, contents in enumerate(sectioned_list):
        for column, value in enumerate(contents):
            #valid diagnoal where column = row, or column + row = matrix_dimensions - 1
            if column == row:
                diag_rows[0].append(value)
            elif column + row == matrix_dimensions - 1:
                diag_rows[1].append(value)
    check = [x for x in diag_rows if np.count_nonzero(x) == 5]
    if len(check) == 1:
        return check[0]
    else:
        return False

def bingo_card_scoring(call_list,bingo_card):
    null_list = [0 for item in range(len(bingo_card))]
    for score, called_number in enumerate(call_list):
        if called_number in bingo_card:
            index = bingo_card.index(called_number)
            null_list[index] = called_number
            summed_remaing_on_board = sum([x for x in bingo_card if x not in null_list])
        if horizontal_check(null_list) is not False:
            return [score,called_number,summed_remaing_on_board,horizontal_check(null_list)]
        if vertical_check(null_list) is not False:
            return [score,called_number,summed_remaing_on_board,vertical_check(null_list)]
        #if diagonal_check(null_list) is not False:
            #return [score,called_number,summed_remaing_on_board,diagonal_check(null_list)]

all_scores = [bingo_card_scoring(bingo_list,card) for card in cards]

#challenge_1
score, multipler, remaining_summed, winning_list = sorted(all_scores, key=lambda x: x[0])[0]
print('challenge_1 answer is '+ str(multipler*remaining_summed))

#challenge_2
score, multipler, remaining_summed, winning_list = sorted(all_scores, key=lambda x: x[0])[-1]
print('challenge_2 answer is '+ str(multipler*remaining_summed))
