user_input = int(input("Enter the number: "))

with open("data.txt", "w") as file:
	for i in range (user_input):
		file.write(str(user_input - i) + "\n")

numbers = []

with open("data.txt", "r") as file:
	numbers = file.read().split("\n")
	numbers.pop()
	
for i in range (len(numbers)):
	print("Line " + str(i + 1) + ":" + numbers[i])