a = (input().split(' '))
a = [int(a[i]) for i in range(len(a))]
r, s, k = a
window = []
for i in range(r):
    window.append(list(input()))

area = (k - 2)
maximum = 0

def countflies(row, column, area):
    count = 0
    for i in range(row, area + row):
        for j in range(column, area + column):
            if(window[i][j] == "*"):
                count += 1

    return count
permrow = 0
permcol = 0
for i in range(1, r - area):
    for j in range(1, s - area):
        flies = countflies(i, j, area)
        if flies > maximum:
            permrow = i
            permcol = j
            maximum = flies

        
permrow = permrow - 1
permcol = permcol - 1
print(maximum)
window[permrow][permcol] = "+"
window[permrow + k - 1][permcol] = "+"
window[permrow][permcol + k - 1] = "+"
window[permrow + k - 1][permcol + k - 1] = "+"

for i in range(1, k - 1):
    window[permrow][permcol + i] = "-"
    window[permrow + k - 1][permcol + i] = "-"
    window[permrow + i][permcol] = "|"
    window[permrow + i][permcol + k - 1] = "|"


for i in window:
    print("".join(i))

