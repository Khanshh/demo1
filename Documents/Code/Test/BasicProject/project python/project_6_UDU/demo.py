import pygame
import csv
import os

# Constants
FILE_NAME = 'qlsv.csv'
WHITE = (245, 245, 245)
BLACK = (30, 30, 30)
BLUE = (70, 130, 180)
LIGHT_GRAY = (220, 220, 220)
BUTTON_COLOR = (100, 149, 237)
BUTTON_HOVER_COLOR = (65, 105, 225)
BUTTON_TEXT_COLOR = WHITE

# Setup Pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Student Management System")

# Load a more readable font
font = pygame.font.SysFont('Arial', 28)
header_font = pygame.font.SysFont('Arial', 36, bold=True)

# Student class
class Student:
    def __init__(self, ID, Name, Class, Age):
        self.ID = ID
        self.Name = Name
        self.Class = Class
        self.Age = Age

# Read students from CSV
def read_students():
    students = []
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode="r", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader, None)  # Skip header
            for row in reader:
                if row:
                    students.append(Student(*row))
    return students

# Write students to CSV
def write_students(students):
    with open(FILE_NAME, mode="w", newline='', encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Name", "Class", "Age"])
        for student in students:
            writer.writerow([student.ID, student.Name, student.Class, student.Age])

# Display centered text on the screen
def display_text(text, x, y, color=BLACK, font=font):
    label = font.render(text, True, color)
    screen.blit(label, (x, y))

# Draw button with hover effect
def draw_button(text, x, y, width, height):
    mouse_x, mouse_y = pygame.mouse.get_pos()
    button_rect = pygame.Rect(x, y, width, height)
    is_hovered = button_rect.collidepoint(mouse_x, mouse_y)

    current_color = BUTTON_HOVER_COLOR if is_hovered else BUTTON_COLOR
    pygame.draw.rect(screen, current_color, button_rect, border_radius=8)
    display_text(text, x + 20, y + 10, BUTTON_TEXT_COLOR)

    return is_hovered and pygame.mouse.get_pressed()[0]

# Draw background
def draw_background():
    screen.fill(WHITE)
    pygame.draw.rect(screen, LIGHT_GRAY, (20, 20, 760, 560), border_radius=15)

# Show all students with horizontal and vertical scrolling
def show_students(students):
    running = True
    scroll_y = 0  # Vertical scroll position
    scroll_x = 0  # Horizontal scroll position
    screen_width = screen.get_width()
    max_scroll_x = 500  # Maximum horizontal scroll distance (limit scroll to prevent infinite scroll)

    # Column widths for spacing
    col_widths = [50, 150, 150, 100]

    while running:
        draw_background()
        display_text("Student List", 100, 30, BLUE, header_font)

        # Draw Back button
        if draw_button("Back", 650, 500, 100, 50):
            running = False

        # Display students with spacing and scroll
        y_offset = 100 + scroll_y  # Adjust y position based on scroll
        for i, student in enumerate(students):
            if 100 <= y_offset <= 500:  # Display only within visible area
                # Adjust each column's x position based on its width
                display_text(f"{i+1}.", 100 + scroll_x, y_offset)  # Index column
                display_text(f"ID: {student.ID}", 100 + col_widths[0] + scroll_x, y_offset)  # ID column
                display_text(f"Name: {student.Name}", 100 + col_widths[0] + col_widths[1] + scroll_x, y_offset)  # Name column
                display_text(f"Class: {student.Class}", 100 + col_widths[0] + col_widths[1] + col_widths[2] + scroll_x, y_offset)  # Class column
                display_text(f"Age: {student.Age}", 100 + col_widths[0] + col_widths[1] + col_widths[2] + col_widths[3] + scroll_x, y_offset)  # Age column
            y_offset += 40  # Line spacing

        # Handle events for scrolling (both vertical and horizontal)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    scroll_y -= 20  # Scroll down vertically
                elif event.key == pygame.K_UP:
                    scroll_y += 20  # Scroll up vertically
                elif event.key == pygame.K_LEFT:
                    scroll_x = max(scroll_x + 20, 0)  # Scroll left horizontally, prevent going negative
                elif event.key == pygame.K_RIGHT:
                    scroll_x = min(scroll_x - 20, max_scroll_x)  # Scroll right horizontally, prevent scrolling too far

        pygame.display.flip()

# Add new student
def add_student(students):
    input_fields = ["Name", "ID", "Age", "Class"]
    inputs = [""] * len(input_fields)
    input_mode = 0
    active = True

    while active:
        draw_background()
        display_text("Add New Student", 100, 30, BLUE, header_font)

        # Draw input fields with spacing
        for i, field in enumerate(input_fields):
            color = BUTTON_HOVER_COLOR if i == input_mode else BUTTON_COLOR
            pygame.draw.rect(screen, color, (100, 100 + i * 70, 400, 40), border_radius=5)
            display_text(f"{field}: {inputs[i]}", 110, 110 + i * 70, WHITE)

        # Draw buttons
        if draw_button("Submit", 550, 450, 200, 50):
            if all(inputs):
                students.append(Student(*inputs))
                write_students(students)
            active = False
        if draw_button("Cancel", 550, 520, 200, 50):
            active = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                active = False
                return students
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    input_mode = (input_mode + 1) % len(input_fields)
                elif event.key == pygame.K_BACKSPACE:
                    inputs[input_mode] = inputs[input_mode][:-1]
                else:
                    inputs[input_mode] += event.unicode

        pygame.display.update()
    return students

# Main loop
def main():
    students = read_students()
    running = True

    while running:
        draw_background()
        display_text("Student Management System", 200, 30, BLUE, header_font)

        # Draw main buttons with spacing
        if draw_button("Add Student", 100, 150, 200, 50):
            students = add_student(students)
        if draw_button("Show Students", 100, 220, 200, 50):
            show_students(students)
        if draw_button("Save & Exit", 100, 290, 200, 50):
            write_students(students)
            running = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()

    pygame.quit()

if __name__ == '__main__':
    main()
