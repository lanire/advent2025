f = open('input.txt', 'r')

entries = []
for i, l in enumerate(f.readlines()):
  l = l.strip()
  direction = l[0]
  n = int(l[1:])
  entries.append((direction, n))

current = 50
count = 0

for e in entries:
    if e[0] == 'R':
        current = (current + e[1])
        if current > 99:
            rots = int(current / 100)
            current = current % 100
            count += rots 
    if e[0] == 'L':
        rot = int(e[1] / 100)
        prev_current = current
        current = (current - (e[1] %100))
        count += rot
        if current == 0:
            count += 1
        if current < 0:
            current = 100 + current
            if prev_current != 0:
                count += 1


print(count)

  
  

  






