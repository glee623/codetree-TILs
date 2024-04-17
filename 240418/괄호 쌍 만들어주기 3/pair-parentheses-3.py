A = list(input())

res = 0
for idx in range(len(A)):
    if A[idx] == '(':
        res += A[idx:].count(')')
print(res)