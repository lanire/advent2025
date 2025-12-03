f = open('input.txt', 'r')

entries = []
for i, l in enumerate(f.readlines()):
  l = l.strip()
  entries.append([int(d) for d in l])

print(entries)


def top_twelve(jolts, remains):
    if remains == 0:
        return 0
    if remains == 1:
        max_v = max(jolts)
    else:
        max_v = max(jolts[0:-(remains-1)])
    max_index = jolts.index(max_v)
    return max_v * 10**(remains -1) + top_twelve(jolts[max_index+1:], remains - 1)


sumt = 0
for e in entries:
    jolt = top_twelve(e, 12)
    sumt += jolt



print(sumt)



  
  

  






