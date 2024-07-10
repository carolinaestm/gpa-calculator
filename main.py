grade_points = {
    'A': 4,
    'B': 3,
    'C': 2,
    'D': 1,
    'F': 0,
    'WF': 0
}
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

def input_courses():
    courses = []
    while True:
        course_name = input("Enter course name (or 'done' to finish): ")
        if course_name.lower() == 'done':
            break
        grade = input("Enter grade received (A, B, C, D, F, WF): ").upper()
        if grade not in grade_points:
            print("Invalid grade entered. Please enter a valid grade.")
            continue
        credit_hours = float(input("Enter credit hours: "))
        courses.append((course_name, grade, credit_hours))
    return courses

def calculate_gpa(courses):
    total_grade_points = 0
    total_credit_hours = 0
    for course_name, grade, credit_hours in courses:
        total_grade_points += grade_points[grade] * credit_hours
        total_credit_hours += credit_hours
    if total_credit_hours > 0:
        gpa = total_grade_points / total_credit_hours
    else:
        gpa = 0
    return gpa
def save_courses(filename, courses):
    with open(filename, 'w') as f:
        for course_name, grade, credit_hours in courses:
            f.write(f"{course_name},{grade},{credit_hours}\n")

def load_courses(filename):
    courses = []
    with open(filename, 'r') as f:
        for line in f:
            course_name, grade, credit_hours = line.strip().split(',')
            credit_hours = float(credit_hours)
            courses.append((course_name, grade, credit_hours))
    return courses
class GPAApp:
    def __init__(self, root):
        self.root = root
        self.root.title("GPA Calculator")

        self.label = tk.Label(self.root, text="Enter your courses and grades to calculate GPA:")
        self.label.pack(pady=10)

        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=10)

        self.course_label = tk.Label(self.frame, text="Course Name:")
        self.course_label.grid(row=0, column=0, padx=10)

        self.grade_label = tk.Label(self.frame, text="Grade (A, B, C, D, F, WF):")
        self.grade_label.grid(row=0, column=1, padx=10)

        self.credit_label = tk.Label(self.frame, text="Credit Hours:")
        self.credit_label.grid(row=0, column=2, padx=10)

        self.course_entry = tk.Entry(self.frame, width=20)
        self.course_entry.grid(row=1, column=0, padx=10)

        self.grade_entry = tk.Entry(self.frame, width=10)
        self.grade_entry.grid(row=1, column=1, padx=10)

        self.credit_entry = tk.Entry(self.frame, width=10)
        self.credit_entry.grid(row=1, column=2, padx=10)

        self.add_button = tk.Button(self.root, text="Add Course", command=self.add_course)
        self.add_button.pack(pady=10)

        self.calculate_button = tk.Button(self.root, text="Calculate GPA", command=self.calculate)
        self.calculate_button.pack(pady=10)

        self.clear_button = tk.Button(self.root, text="Clear All", command=self.clear_entries)
        self.clear_button.pack(pady=10)

        self.save_button = tk.Button(self.root, text="Save Courses", command=self.save_courses_gui)
        self.save_button.pack(pady=10)

        self.load_button = tk.Button(self.root, text="Load Courses", command=self.load_courses_gui)
        self.load_button.pack(pady=10)

        self.courses = []

    def add_course(self):
        course_name = self.course_entry.get()
        grade = self.grade_entry.get().upper()
        credit_hours = float(self.credit_entry.get())

        if grade not in grade_points:
            messagebox.showerror("Error", "Invalid grade entered. Please enter a valid grade.")
            return

        self.courses.append((course_name, grade, credit_hours))
        messagebox.showinfo("Course Added", f"{course_name} added successfully.")
        self.clear_entries()

    def calculate(self):
        if not self.courses:
            messagebox.showwarning("No Courses", "Please add courses before calculating GPA.")
            return

        gpa = calculate_gpa(self.courses)
        messagebox.showinfo("GPA Calculated", f"Your GPA is: {gpa:.2f}")

    def clear_entries(self):
        self.course_entry.delete(0, tk.END)
        self.grade_entry.delete(0, tk.END)
        self.credit_entry.delete(0, tk.END)

    def save_courses_gui(self):
        filename = tk.filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if filename:
            save_courses(filename, self.courses)
            messagebox.showinfo("Courses Saved", "Courses saved successfully.")

    def load_courses_gui(self):
        filename = tk.filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if filename:
            self.courses = load_courses(filename)
            messagebox.showinfo("Courses Loaded", "Courses loaded successfully.")

if __name__ == "__main__":
    root = tk.Tk()
    app = GPAApp(root)
    root.mainloop()
