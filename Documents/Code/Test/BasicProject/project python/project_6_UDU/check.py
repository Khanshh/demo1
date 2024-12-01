from tabulate import tabulate
import csv

FILE_NAME = 'schedule.csv'	

class School_Schedule:
	def __init__(self, Day, Start, End, Course):
		self.Day = Day
		self.Start = Start
		self.End = End
		self.Course = Course

def read_schedule():
	Day = input("Enter Day: ")
	Start = input("Enter Start: ")
	End = input("Enter End: ")
	Course = input("Enter Course: ")
	schedule = School_Schedule(Day, Start, End, Course)

	return schedule
	
def print_schedule(schedule):
	print("Day :", schedule.Day)
	print("Start: ", schedule.Start)
	print("End: ", schedule.End)
	print("Course: ", schedule.Course)

def read_schedules():
	schedules = []
	total_schedules = 7
	for i in range(total_schedules):
		print("Schedule" + str(i + 1))
		schu = read_schedule()	
		schedules.append(schu)
	return schedules	

def print_schedules_table(schedules):
	table = []
	for i, schedule in enumerate(schedules, start = 1):
			table.append([i, schedule.Day, schedule.Start, schedule.End, schedule.Course])

	headers = ["#", "Day", "Start Time", "End Time", "Course"]
	print("\n")
	print("=== School Schedule ===")
	print(tabulate(table, headers, tablefmt="grid"))

def write_schedules_to_csv(schedules):
	with open(FILE_NAME, mode = "w", newline='', encoding="utf-8") as file:
		writer = csv.writer(file)
		writer.writerow(["Day", "Start", "End", "Course"])
		for schedule in schedules:
			writer.writerow([schedule.Day, schedule.Start, schedule.End, schedule.Course])

def read_schedules_to_csv():
	schedules = []
	with open(FILE_NAME, mode = 'r', newline = '', encoding = 'utf-8') as file:
		reader = csv.reader(file)
		next(reader)
		for row in reader:
			if len(row) == 4:
				schedules.append(School_Schedule(row[0], row[1], row[2], row[3]))

	return schedules

def select_in_range(prompt, min, max):
	choice = input(prompt)
	while not choice.isdigit() or int(choice) < min or int(choice) > max:
		choice = input(prompt)

	choice = int(choice)
	return choice	

def menu():
	print("------|Creative to schedule|-------")
	print("| Option 1: Creative to schedules.|")
	print("| Option 2: Show schedule.        |")
	print("| Option 3: Add schedule.         |")
	print("| Option 4: Update schedules.     |")
	print("| Option 5: Delete schedules.     |")
	print("| Option 6: Save to Exit.         |")
	print("-----------------------------------")

def main():
	while True:

		try:
			schedules = read_schedules_to_csv()
			print("Loadinggg...........")
		except:
			print("Welcome, first user!!")			
		
		menu()
	
		choice = select_in_range("Select a option (1 - 6): ", 1, 6)

		if choice == 1:
			schedules = read_schedules()
		try:
			if choice == 2:
				print_schedules_table(schedules)
				input("\nPress Enter to continue.\n")				
			elif choice == 6:
				write_schedules_to_csv(schedules)
				input("\nPress Enter to continue.\n")
				break

		except:
			print("0----0")
			break		

main()