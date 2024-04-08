N = int(input())

x, y = 0,0
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1] # 동남서북
for n in range(N):
    way, step = input().split()
    step = int(step)
    if way == 'W':
        nx, ny = x + dx[2]*step, y + dy[2]*step
        x, y = nx, ny
    elif way == 'S':
        nx, ny = x + dx[1]*step, y + dy[1]*step
        x, y = nx, ny
    elif way == 'N':
        nx, ny = x + dx[3]*step, y + dy[3]*step
        x, y = nx, ny
    elif way == 'E':
        nx, ny = x + dx[0]*step, y + dy[0]*step
        x, y = nx, ny

print(x, y)