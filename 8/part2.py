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


num_coords = len(entries)

prev_coords = set()
coords = None
i = 0
while len(circuits[entries[0]]) < num_coords:
    print('iteration %d' %i)
    i+=1
    min_dist = 10000000000000
    for e in entries:
        for g in entries:
            if e != g and (e, g) not in prev_coords and (g, e) not in prev_coords:
                dist = distance(e, g)
                if dist < min_dist:
                    min_dist = dist
                    coords = (e, g)

    prev_coords.add(coords)
    prev_f = circuits[coords[0]]
    prev_g = circuits[coords[1]]

    ns = prev_f.union(prev_g)

    for n in ns:
        circuits[n] = ns

print(coords[0][0] * coords[1][0])

#v = circuits.values()
#v = sorted(v, key=len, reverse=True)
#uniq = []
#for a in v:
#  if a not in uniq:
#    uniq.append(a)

#print(uniq[0])
#print(uniq[1])
#print(uniq[2])

#print(len(uniq[0]) * len(uniq[1]) * len(uniq[2]))


