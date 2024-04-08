n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

dxs = [1, -1, 0, 0]
dys = [0, 0, -1, 1]

def in_range(x, y):
    return 0<=x<n and 0<=y<n

def adjacent_cnt(x, y):
    cnt = 0
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if in_range(nx, ny) and arr[nx][ny]:
            cnt += 1
    return cnt

answer = 0
for i in range(n):
    for j in range(n):
        if adjacent_cnt(i, j) >= 3:
            answer += 1

print(answer)