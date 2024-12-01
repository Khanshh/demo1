import os
import csv
import random

#os.mkdir("exc_qlsv")

qlsv = open("qlsv.csv", mode = "r", encoding = "utf-8-sig")

qlsv_01 = open("exc_qlsv/D24CQCC01-B.csv", mode = "w", encoding = "utf-8-sig", newline = "")
qlsv_05 = open("exc_qlsv/D24CQCC05-B.csv", mode = "w", encoding = "utf-8-sig", newline = "")
qlsv_06 = open("exc_qlsv/D24CQCC06-B.csv", mode = "w", encoding = "utf-8-sig", newline = "")

csv_qlsv = csv.reader(qlsv)
csv_qlsv_01 = csv.writer(qlsv_01)
csv_qlsv_05 = csv.writer(qlsv_05)
csv_qlsv_06 = csv.writer(qlsv_06)

header = ["Ten", "Ma", "Tuoi", "Lop", "Diem Danh", "Diem Chuyen Can", "Giua Ki", "Cuoi Ki"] 

for csv in [csv_qlsv_01, csv_qlsv_05, csv_qlsv_06]:
	csv.writerow(header)

for s in csv_qlsv:
	random_point = [s[0], s[1], s[2], s[3]]
	random_point.append(round(random.uniform(4, 10), 1))
	random_point.append(round(random.uniform(4, 10), 1))
	random_point.append(round(random.uniform(4, 10), 1))
	random_point.append(round(random.uniform(4, 10), 1))


	if s[3] == "D24CQCC01-B":
		csv_qlsv_01.writerow(random_point)
	if s[3] == "D24CQCC05-B":
		csv_qlsv_05.writerow(random_point)
	if s[3]	== "D24CQCC06-B":
		csv_qlsv_06.writerow(random_point)


