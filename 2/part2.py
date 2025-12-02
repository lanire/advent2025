f = open('input.txt', 'r')

def is_valid(number):
    str_num = str(number)
    length = len(str_num)
    for i in range(2, length + 1): # number of repeats 2-length
        interval = int(length/i) # size of each repeat
        if interval < 1:
            break
        start = str_num[0:interval]
        match = True
        j = 1
        while (j*interval < length):
            s = j*interval
            e = j*interval + interval
            j = j+1
            if (str_num[s : e] != start):
                match = False
                break
        if match:
            return False 
    return True

entries = []
for i, l in enumerate(f.readlines()):
  l = l.strip()
  ranges = l.split(',')
  for r in ranges:
      start, end = r.split('-')
      entries.append((int(start), int(end)))


sum = 0
for e in entries:
    for i in range(e[0], e[1] + 1, 1):
        if not is_valid(i):
            sum += i

print("The sum is ")
print(sum)



  
  

  






