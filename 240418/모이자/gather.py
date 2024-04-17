import sys

n = int(input())
arrs = list(map(int,input().split()))

min_res = sys.maxsize
for i in range(n):
    diff = 0
    for j in range(n):
        diff += (arrs[j]*abs(i-j))
    min_res = min(min_res, diff)
print(min_res)