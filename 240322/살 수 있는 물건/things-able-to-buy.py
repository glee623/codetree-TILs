lists = {'book':3000, 'mask':1000}
lists = sorted(lists.items(), key = lambda d:d[1], reverse = True )

n = int(input())
for thing,price in lists:
    if price <= n:
        print(thing)
        break