N = int(input())
arrs = [list(map(int, input().split())) for _ in range(N)]

max_res = 0
for i in range(N):
    for j in range(N-2):
        max_res = max(max_res,sum([arrs[i][j+k] for k in range(3)]))
print(max_res)