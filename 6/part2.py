f = open('input.txt', 'r')

entries = []
file = f.readlines()

for i, l in enumerate(file):
    entries.append(l[:-1])


ops = entries[len(entries)-1].split()
op_id = len(ops) - 1


nums = []
total = 0
for i in range(len(entries[0]) - 1, -1, -1):
    number = entries[0][i]
    for j in range(1, len(entries) - 1):
        number += entries[j][i]
    number = number.strip()
    if i == 0:
        nums.append(int(number))
    if number == '' or i == 0:
        op = ops[op_id]
        op_id -= 1
        inter = 0
        if op == '+':
            inter = sum(nums)
        elif op == '*':
            inter = nums[0]
            for j in range(1, len(nums)):
                inter *= nums[j]
        total += inter
        nums = []
    else:
        number = int(number)
        nums.append(number)

print(total)





