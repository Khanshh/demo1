import csv

# Khởi tạo file CSV để lưu trữ dữ liệu học sinh
FILE_NAME = 'students.csv'

def initialize_csv():
    with open(FILE_NAME, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Name", "Age", "Class"])

# Thêm học sinh mới
def add_student(student_id, name, age, student_class):
    with open(FILE_NAME, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([student_id, name, age, student_class])
    print("Added student successfully.")

# Xem danh sách học sinh
def view_students():
    with open(FILE_NAME, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

# Cập nhật thông tin học sinh
def update_student(student_id, name=None, age=None, student_class=None):
    students = []
    with open(FILE_NAME, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == student_id:
                if name:
                    row[1] = name
                if age:
                    row[2] = age
                if student_class:
                    row[3] = student_class
            students.append(row)

    with open(FILE_NAME, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(students)
    print("Updated student successfully.")

# Xóa học sinh
def delete_student(student_id):
    students = []
    with open(FILE_NAME, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] != student_id:
                students.append(row)

    with open(FILE_NAME, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(students)
    print("Deleted student successfully.")

# Menu điều khiển
def menu():
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

# Hàm chính
def main():
    initialize_csv()
    while True:
        menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            student_id = input("Enter student ID: ")
            name = input("Enter student name: ")
            age = input("Enter student age: ")
            student_class = input("Enter student class: ")
            add_student(student_id, name, age, student_class)
        elif choice == '2':
            view_students()
        elif choice == '3':
            student_id = input("Enter student ID to update: ")
            name = input("Enter new name (leave blank to keep current): ")
            age = input("Enter new age (leave blank to keep current): ")
            student_class = input("Enter new class (leave blank to keep current): ")
            update_student(student_id, name or None, age or None, student_class or None)
        elif choice == '4':
            student_id = input("Enter student ID to delete: ")
            delete_student(student_id)
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
