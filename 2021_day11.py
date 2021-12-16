import numpy as np
import io

content = []
with io.open("filepath/input_d11.txt", "r", newline=None) as fd:
    for line in fd:
        line = line.replace("\n", "")
        content.append([int(point) for point in line])
content = np.array(content)

def fill(matrix,starting_tuple):
    width,height = matrix.shape
    queue = []
    queue.append(starting_tuple)
    while len(queue) > 0:
        x,y = queue.pop(0)
        neighbors = [(x-1,y),(x+1,y),(x-1,y-1),(x+1,y+1),(x-1,y+1),(x+1,y-1),(x,y-1),(x,y+1)]
        for n in neighbors:
            if 0 <= n[0] <= width-1 and 0 <= n[1] <= height-1:
                matrix[n] += 1
                if matrix[n] == 10:
                    queue.append(n)

def flash_steps(matrix,steps):
    flashes_count = 0
    while steps > 0:
        matrix += 1
        flashed_octopi = set()
        octopi_greater_than_9 = np.transpose((matrix>9).nonzero()).tolist() # gets all x,y pairs greater than 9
        for coors in octopi_greater_than_9:
            fill(matrix,tuple(coors))
        increase = len(np.transpose((matrix>9).nonzero()).tolist())
        flashes_count += increase
        matrix[matrix > 9] = 0
        steps += -1
    return flashes_count

def flash_steps_sync(matrix):
    steps_count = 1
    while True:
        matrix += 1
        octopi_greater_than_9 = np.transpose((matrix>9).nonzero()).tolist() # gets all x,y pairs greater than 9
        for coors in octopi_greater_than_9:
            fill(matrix,tuple(coors))
        increase = len(np.transpose((matrix>9).nonzero()).tolist())
        matrix[matrix > 9] = 0
        zeros = np.zeros(matrix.shape)
        #if increase == 100:
        if (matrix == zeros).all():
            return steps_count
        else:
            steps_count += 1

print('Part 1 is: ',flash_steps(np.copy(content),100))
print('Part 2 is: ', flash_steps_sync(np.copy(content)))
