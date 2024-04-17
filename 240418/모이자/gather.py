n = int(input())
arrs = list(map(int, input().split()))

max_res = -9999
for i in range(n):
    arrs[i] *= 2
    diff = 0
    for j in range(n-1):
        diff += abs(arrs[j+1]-arrs[j])

    if max_res < diff:
        max_res = diff
    arrs[i] //= 2

print(max_res)