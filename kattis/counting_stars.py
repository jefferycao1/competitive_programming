import sys
sys.setrecursionlimit(10**6)


stars = 0
def replacestar(sky, i, j):
    sky[i][j] = str(stars)
    if(j != 0 and sky[i][j-1] == "-"):
        replacestar(sky, i, j-1)
    if(j != n - 1 and sky[i][j+1] == "-"):
        replacestar(sky, i, j+1)
    if(i != 0 and sky[i-1][j] == "-"):
        replacestar(sky, i-1, j)
    if(i != m - 1 and sky[i + 1][j] == "-"):
        replacestar(sky, i+1, j)
    

line = input()
count = 1
while(line != ""):
        
        m, n = [int(x) for x in line.split()]
        sky = []
        stars = 0
        for i in range(m):
            sky.append(list(input()))



        for i in range(m):
            for j in range(n):
                if(sky[i][j] == "-"):
                    replacestar(sky, i, j)
                    stars += 1
        print(f"Case {count}: {stars}")
        line = input()
        count += 1
