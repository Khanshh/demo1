def calc_number(n):
	total = 0
	if n % 2 == 1:
		for i in range(1, n + 1, 2):
			total += 1/i 
	else:
		for i in range(2, n + 1, 2):
			total += 1/i
	total = round(total, 6)		
	return total	
	
for t in range(int(input())):
	n = int(input())
	print(calc_number(n))
