f = open('input.txt', 'r')


entries = []
for i, l in enumerate(f.readlines()):
  l = l.strip()
  entries.append([c for c in l])


def is_paper(grid, i, j):
    if i < 0:
        return False
    if i >= len(grid):
        return False
    if j < 0:
        return False
    if j >= len(grid[0]):
        return False
    return grid[i][j] == '@'

def can_access(grid, i, j):
    ct = 0
    for k in (-1, 0, 1):
        for l in (-1, 0, 1):
            if k == 0 and l == 0:
                continue
            ip = is_paper(grid, i+k, j+l)
            if ip:
                ct += 1
    return ct < 4

count = 0
for i, e in enumerate(entries):
    for j, c in enumerate(e):
        if entries[i][j] == '@':
            ca = can_access(entries, i, j) 
            if ca:
                print('coord: (%d, %d)' %(i, j))
                count += 1
            

print(count)




  
  

  






