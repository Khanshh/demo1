s = input()
number_lucky = 0

for i in range(len(s)):
	if s[i] == '4' or s[i] == '7':
		number_lucky += 1

if number_lucky == 4 or number_lucky == 7:
	print("YES")
else:
	print("NO")	