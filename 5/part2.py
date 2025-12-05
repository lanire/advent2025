f = open('input.txt', 'r')


ranges = []
ingr = []
parse_ranges = True
for i, l in enumerate(f.readlines()):
  l = l.strip()
  if l == '':
      parse_ranges = False
      continue

  if parse_ranges:
      first, last = l.split('-')
      ranges.append([int(first), int(last)])
  else:
      ingr.append(int(l))

ranges = sorted(ranges)

i = 0
while i < len(ranges) - 1:
    next_start = ranges[i+1][0]
    if next_start >= ranges[i][0] and next_start <= ranges[i][1]:
        # overlap in ranges, merge together
        if ranges[i+1][1] <= ranges[i][1]:
            # the range is contained within this one, just delete it
            ranges.remove(ranges[i+1])
        elif ranges[i+1][1] > ranges[i][1]:
            # the range is longer, switch to the longer length
            ranges[i][1] = ranges[i+1][1]
            ranges.remove(ranges[i+1])
    else:
        # no overlap, move to next
        i += 1


size = 0
for r in ranges:
    size += (r[1] - r[0] + 1)

        
print(size)




