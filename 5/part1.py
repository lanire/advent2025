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
      ranges.append((int(first), int(last)))
  else:
      ingr.append(int(l))

ranges = sorted(ranges)


def is_in_range(ingr, ranges):
    for r in ranges:
        if r[0] > ingr:
            return False
        if r[0] <= ingr and r[1] >= ingr:
            return True
    return False

count = 0
for i in ingr:
    tf = is_in_range(i, ranges)
    if tf:
        count+=1

print(count)




