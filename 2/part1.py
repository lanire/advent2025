f = open('input.txt', 'r')

def is_valid(number):
    str_num = str(number)
    length = len(str_num)
    hl = int(length/2)
    f_half = str_num[0:hl]
    s_half = str_num[hl:]
    return f_half != s_half

entries = []
for i, l in enumerate(f.readlines()):
  l = l.strip()
  ranges = l.split(',')
  for r in ranges:
      start, end = r.split('-')
      entries.append((int(start), int(end)))

print(entries)

sum = 0
for e in entries:
    for i in range(e[0], e[1] + 1, 1):
        if not is_valid(i):
            print(i)
            sum += i

print("The sum is ")
print(sum)



  
  

  






