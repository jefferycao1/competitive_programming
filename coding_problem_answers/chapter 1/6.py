# -*- coding: utf-8 -*-
def compress(str1):
    length = len(str1)
    newstr = ""
    currentnum = 1
    for i in range(len(str1)):
        if(i == len(str1) - 1):
            newstr += str1[i] + str(currentnum)
        else:
            if(str1[i] == str1[i + 1]):
                currentnum += 1
                continue
            else:
                newstr += (str1[i] + str(currentnum))
                currentnum = 1
                continue


    if(length > len(newstr)):
         return newstr
    else:
         return str1

if __name__ == "__main__":
    str1 = "aabcccccaaa"
    print(compress(str1))