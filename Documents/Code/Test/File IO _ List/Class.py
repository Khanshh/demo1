class Student:
	def __init__(self, name, age, math, english):
		self.name = name
		self.age = age
		self.math = math
		self.english = english

	def total_score(self):
		total = (self.math + self.english) / 2
		return total

s1 = Student("Khanh", 18, 9, 10) 

print(s1.total_score()) 
