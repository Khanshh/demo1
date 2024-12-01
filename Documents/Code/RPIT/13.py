def greatest_common_wish(a, b):
	r = a % b 
	while r != 0:
		a = b
		b = r
		r = a % b
	return b

def sum_greatest_common_wish(b):
	total = sum(int(digit) for digit in str(b))
	return total

def is_prime(total):
	if total < 2:
		return "NO"
	for i in range(2, int(total**0.5) + 1):
		if total % i == 0:
			return "NO"
	return "YES"


for t in range(int(input())):
	a, b = [int(i) for i in input().split()]
	b = greatest_common_wish(a, b)
	total = sum_greatest_common_wish(b)
	print(is_prime(total))
	