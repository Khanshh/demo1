print("What your name? ")
name = input()

print("What is your score in 3 subjects?")
print("math: ")
math = input()
math = float(math)
print("english: ")
english = input()
print("vietnames: ")
vietnames = input()

total = (math + float(vietnames)) * 2 + float(english)
total = float(total)

print("What is your school's benchmark?")
benchmark = input()
benchmark = float(benchmark) 

print("-------")
print("Your name " + name)
print("Your total score is: " + str(total))

print("------ ")
print(" ---")
print("  -")

if total<benchmark:
	print("You have failed :(")
else:
	print("You pass :)")



