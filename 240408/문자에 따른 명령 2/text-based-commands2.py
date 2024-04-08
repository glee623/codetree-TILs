sen = list(input())

x, y = 0,0
dx, dy = 0, 1
for char in sen:
    if char == 'L':
        dx, dy = dy *-1, dx
    elif char == 'R':
        dx, dy = dy, dx *-1
    else:
        x += dx
        y += dy
print(x,y)