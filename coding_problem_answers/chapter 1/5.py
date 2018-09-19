# -*- coding: utf-8 -*-
from collections import Counter

def oneoff(a, b):
    acount = Counter(a)
    bcount = Counter(b)
    
    difference = 0
    iterate = acount if len(acount) > len(bcount) else bcount
    
    for i in iterate:
        difference += abs(acount[i] - bcount[i])
    
    if(difference > 1):
        return False
    else:
        return True
    
    



if __name__ == "__main__":
    str1 = "pale"
    str2 = "bake"
    print(oneoff(str1, str2))
    
