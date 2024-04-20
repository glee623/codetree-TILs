def print_rec(N):
    cnt = 1
    for i in range(N):
        for j in range(N):
            print(cnt, end = " ")
            cnt += 1
            if cnt == 10:
                cnt = 1
        print()

N = int(input())
print_rec(N)