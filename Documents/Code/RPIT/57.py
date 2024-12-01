def is_prime(digit):
	return digit in {'2', '3', '5','7'}
	
def check_is_prime(n):
	for i in range(len(n)):
		if i in [2, 3, 5, 7]:
			if not is_prime(n[i]):
				return False
		else:
			if is_prime(n[i]):
				return False
	return True		

for t in range(int(input())):
	n = input()			 	
	if check_is_prime(n):
		print("YES")
	else:
		print("NO")	