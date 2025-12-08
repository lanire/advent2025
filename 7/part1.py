f = open('input.txt', 'r')


grid = []
start_index = -1
indecies = []
for l in f.readlines():
    if 'S' in l:
        start_index = l.find('S')
        indecies = [start_index]

    l = [n for n in l.strip()]
    grid.append(l)


current_row = 0
next_indecies = []
count = 0
while current_row < len(grid) - 1:
    for ind in indecies:
        if (grid[current_row + 1][ind]) == '.':
           next_indecies.append(ind)
        elif (grid[current_row + 1][ind]) == '^':
            if ind > 0:
                next_indecies.append(ind - 1)
            if ind < len(grid[0]) - 1:
                next_indecies.append(ind + 1)
                count += 1
    indecies = sorted(list(set(next_indecies))) 
    next_indecies = []
    current_row += 1

print(count)
