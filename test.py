from functools import reduce

n = 5
l = [0]
for i in range(1, n + 1):
    nums = list(map(int, list(bin(i)[2:])))
    l.append(reduce(lambda x,y: x+y, nums,0))
print(l)