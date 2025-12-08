import math
import functools

f = open('input.txt', 'r')

circuits = {} 

entries = []
for l in f.readlines():
    l = l.strip()
    x, y, z = l.split(',')
    coord = (int(x), int(y), int(z))
    entries.append(coord)
    circuits[coord] = {coord}


@functools.lru_cache(maxsize=None)
def distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2 + (c1[2] - c2[2])**2)



prev_coords = set()
for i in range(0, 1000):
    print('iteration %d' %i)
    min_dist = 10000000000000
    coords = []
    for e in entries:
        for g in entries:
            if e != g and (e, g) not in prev_coords and (g, e) not in prev_coords:
                dist = distance(e, g)
                if dist < min_dist:
                    min_dist = dist
                    coords = (e, g)

    
    print('here')
    prev_coords.add(coords)
    prev_f = circuits[coords[0]]
    prev_g = circuits[coords[1]]

    ns = prev_f.union(prev_g)
    print('here2')

    for n in ns:
        circuits[n] = ns


v = circuits.values()
v = sorted(v, key=len, reverse=True)
uniq = []
for a in v:
  if a not in uniq:
    uniq.append(a)

print(uniq[0])
print(uniq[1])
print(uniq[2])

print(len(uniq[0]) * len(uniq[1]) * len(uniq[2]))


