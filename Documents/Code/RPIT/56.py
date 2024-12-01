def check_number(n):
	list_n = list(n)
	for i in range(0, len(n), 2):
		if int(list_n[i]) % 2 != 0:
			return False

	for i in range(1, len(n), 2):
		if int(list_n[i]) % 2 != 1:
			return False

	def is_prime(total):
		if total < 2:
			return False
		for i in range(2, int(total ** 0.5) + 1):
			if total == i:
				return False
	
	return True

def sum_n(n):
	total = sum(int(i) for i in str(n))
	return total

for t in range(int(input())):
	n = input()
	total = sum_n(n)
	if check_number(n):
		print("YES")
	else:
		print("NO")