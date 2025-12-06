f = open('input.txt', 'r')

entries = []
file = f.readlines()

for i, l in enumerate(file):
  if l.startswith('*') or l.startswith('+'):
      n1 = l.split()
  else:
      n1 = [int(n) for n in l.split()]
  entries.append(n1)

print(entries)

sum = 0
for i in range(len(entries[0])):
    op = entries[len(entries) - 1][i]
    inter = entries[0][i]
    for j in range(1, len(entries) - 1):
        if op == '*':
            inter = inter * entries[j][i]
        elif op == '+':
            inter = inter + entries[j][i]
    sum += inter


print(sum)

