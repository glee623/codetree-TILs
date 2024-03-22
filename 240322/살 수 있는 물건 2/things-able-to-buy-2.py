lists = {'book':3000, 'mask':1000, 'pen':500}
lists = sorted(lists.items(), key = lambda d:d[1], reverse = True )

n = int(input())
out = 'no'
for thing,price in lists:
    if price <= n:
        out = thing
        break
print(out)