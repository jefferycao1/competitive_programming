s, c, k = [int(x) for x in input().split()]

num = 1
d = [int(x) for x in input().split()]

d.sort()
batch = 0
minimum = d[0]
for i in range(0, len(d)):
    if(batch >= c):
        num += 1
        batch = 0
        minimum = d[i]
    
    if(d[i] - minimum <= k):
        batch += 1
    elif(d[i] - minimum > k):
        num += 1
        batch = 1
        minimum = d[i]

        

print(num)
