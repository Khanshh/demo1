def sum_product(n):
	add = 1
	core = 0 
	for i in range(len(n)):
		if i % 2 == 1:
			core += int(n[i])
		else:
			if n[i] != '0':
				add *= int(n[i])
 
	paste = str(add) + " " + str(core)
	return paste

for i in range(int(input())):
	n = input()
	print(sum_product(n))		

