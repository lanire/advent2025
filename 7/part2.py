import functools

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


@functools.lru_cache(maxsize=None)
def get_num_splits(row, col):
    if row > len(grid) - 1:
        return 1
    if col > len(grid[0]) - 1:
        return 1
    if col < 0:
        return 1
    if grid[row][col] != '^':
        return get_num_splits(row + 1, col)
    else:
        return get_num_splits(row + 1, col + 1) + get_num_splits(row + 1, col - 1)


print(get_num_splits(0, start_index))
