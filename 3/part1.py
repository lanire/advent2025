f = open('input.txt', 'r')


entries = []
for i, l in enumerate(f.readlines()):
  l = l.strip()
  entries.append([int(d) for d in l])

print(entries)

sumt = 0
for e in entries:
    max_v = max(e)
    max_index = e.index(max_v)
    if max_index == len(e) - 1:
        max_v = max(e[0:-1])
        max_index = e.index(max_v)
    max_v2 = max(e[max_index+1:])
    jolt = max_v * 10 + max_v2
    print(jolt)
    sumt += jolt



print(sumt)



  
  

  






