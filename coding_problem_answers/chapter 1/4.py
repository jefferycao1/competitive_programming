from collections import Counter

def Palindrome(str1):
	str1 = str1.lower().replace(" ", "")
	c = Counter(str1)
	odd_counter = 0
	for key in c:
		if (c[key] % 2 == 1):
			odd_counter += 1

	if(odd_counter > 1):
		return False
	return True

def Palindromedict(str1):
    str1 = str1.lower().replace(" ", "")
    c = {}
    for i in str1:
        if i not in c:
            c[i] = 1
        else:
            c[i] += 1
    odd_counter = 0
    for key, value in c.items():
        if(value % 2 == 1):
            odd_counter += 1
        print(value)
    if(odd_counter > 1):
        return False
    return True


if __name__ == "__main__":
	a = "Tact Coa"
	print(Palindromedict(a))
    
    