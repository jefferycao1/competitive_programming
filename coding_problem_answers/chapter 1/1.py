s = "asdfbB"
a = []

for i in range(len(s)):
	if(s[i] in a):
		print("failed")
		break
	else:
		a.append(s[i])
else:
	print("All unique")

