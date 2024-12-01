def check_string(s):
	n = str(s)
	if int(len(s)) % 2 == 0:
		return False

	if s[0] == s[1]:
		return False

	for i in range(0, len(s), 2):
		if n[i] != n[0]:
			return False

	return True

for i in range(int(input())):
	s = input()
	if check_string(s):
		print('YES')
	else:
		print('NO')

