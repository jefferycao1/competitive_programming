n = int(input())
for i in range(n):
    line = str(input()).lower()
    a  = 'abcdefghijklmnopqrstuvwxyz'
    for i in line:
        if (i in a):
            a = a.replace(i, "")

    if(a == ""):
        print("pangram")
    else:
        print("missing",a)
