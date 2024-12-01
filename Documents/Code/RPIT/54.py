def product(n):
	core = 1 
	for i in range(len(n)):
		if n[i] != '0':
			core *= int(n[i])
	return core

for t in range(int(input())):
	n = input()
	print(product(n))
