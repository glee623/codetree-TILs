sen = list(input())

x, y = 0,0
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
move = 3
for char in sen:
    if char == 'L':
        move =(move -1 +4) % 4
    elif char == 'R':
        move =(move +1) % 4
    else:
        x = dx[move]
        y = dy[move]
        
print(x,y)