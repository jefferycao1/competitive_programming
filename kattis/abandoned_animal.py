n = int(input())
k = int(input())

stores = {}
for i in range(k):
    line = input().split()
    number = int(line[0])
    item = line[1]

    if(item in stores.keys()):
        stores[item].append(number)
    else:
        stores[item] = [number]

for k, v in stores.items():
    v = v.sort()
m = int(input())

order = []
for i in range(m):
    order.append(input())



try:
    current = 0
    currentpath = []
    for item in order:
        while(stores[item][0] < current):
            stores[item].pop(0)
        current = stores[item].pop(0)
        currentpath.append(current)
except:
    print("impossible")
else:
    highest = 100000000000
    while(currentpath):
        item = order.pop()
        if(stores[item] and highest >= stores[item][0]):
            print("ambiguous")
            break
        highest = currentpath.pop()
    else:
        print("unique")
         
