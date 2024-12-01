import datetime

def ask_person_info():
	firstname = input("Firstname : ")
	lastname = input("Lastname : ")
	age = int(input("How old are you : "))
	height = input("What is your approximate height?\n")
	weight = input("What is your approximate weight?\n")
	is_male = ask_no_yes("What is male (yes/no): ")
	return firstname, lastname, age, height, weight, is_male

def ask_no_yes(prompt):
	while True:
		answer = input(prompt)
		if answer == "yes" or answer == "Y" or answer == "Yes" or answer == "y":
			return True
		elif answer == "no" or answer == "N" or answer == "No" or answer == "n":	
			return False
		else:
			continue

def calc_year(age):
	now = datetime.datetime.now()
	CURRENT_YEAR = now.year
	return CURRENT_YEAR - age

def calc_BMI(weight, height):
	BMI = float(weight) / (float(height) * float(height))
	BMI = round(BMI,2)
	return BMI

def BMI_info(BMI, is_male, age):
	if BMI < 18.5:
		print("you are" , end = " ")

		for x in range(10):
			print("very" , end = " ")

		print("skinny!!!!")

	elif BMI >= 18 and BMI < 25:
		print("Your weight is normal")
	else:
		print("You are overweight")

	if is_male == True and age >= 18:
		print("You are a grown man")
	elif is_male == False  and age >= 18:
		print("You are a grown woman")
	elif is_male == True and age < 18:
		print("You are a boy")
	elif is_male == False and age < 18:
		print("You are a girl")

def print_person_info(firstname, lastname, age, height, weight, is_male, year, BMI):
	print("-------")
	print("Your name is {1} {0}".format(firstname,lastname))
	print("Your age " + str(age))
	print("Your born year " + str(year))
	print("Your BMI " + str(BMI))
	print("-------")

def main():
	firstname, lastname, age, height, weight, is_male = ask_person_info()
	year = calc_year(age)
	BMI = calc_BMI(weight, height)
	print_person_info(firstname, lastname, age, height, weight, is_male, year, BMI)
	BMI_info(BMI, is_male, age)

main()





