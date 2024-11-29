import tkinter as tk
from tkinter import messagebox, simpledialog, ttk

class StudentManagementSystem:
    def __init__(self, master):
        self.master = master
        self.master.title("Student Management System")
        self.file_name = "students.txt"
        self.master.geometry("520x450")
        self.master.iconbitmap("gcem.ico")
        self.create_ui()
        

    def create_ui(self):
        self.roll_no_var = tk.StringVar()
        self.name_var = tk.StringVar()
        self.gender_var = tk.StringVar()
        self.cgpa_var = tk.StringVar()
        self.semester_var = tk.StringVar()
        self.dob_var = tk.StringVar()
        self.mobile_var = tk.StringVar()
        self.pmobile_var = tk.StringVar()
        self.email_var = tk.StringVar()

        tk.Label(self.master, text="USN:").grid(row=0, column=0, padx=10, pady=10)
        tk.Entry(self.master, textvariable=self.roll_no_var).grid(row=0, column=1, padx=10, pady=10)

        tk.Label(self.master, text="Name:").grid(row=1, column=0, padx=10, pady=10)
        tk.Entry(self.master, textvariable=self.name_var).grid(row=1, column=1, padx=10, pady=10)

        tk.Label(self.master, text="Gender:").grid(row=2, column=0, padx=10, pady=10)
        tk.Radiobutton(self.master, text="Male", variable=self.gender_var, value="Male").grid(row=2, column=1)
        tk.Radiobutton(self.master, text="Female", variable=self.gender_var, value="Female").grid(row=2, column=2)

        tk.Label(self.master, text="CGPA:").grid(row=3, column=0, padx=10, pady=10)
        tk.Entry(self.master, textvariable=self.cgpa_var).grid(row=3, column=1, padx=10, pady=10)

        tk.Label(self.master, text="Semester:").grid(row=4, column=0, padx=10, pady=10)
        ttk.Combobox(self.master, textvariable=self.semester_var, values=[1, 2, 3, 4, 5, 6, 7, 8]).grid(row=4, column=1, padx=10, pady=10)

        tk.Label(self.master, text="Date of Birth:").grid(row=5, column=0, padx=10, pady=10)
        tk.Entry(self.master, textvariable=self.dob_var).grid(row=5, column=1, padx=10, pady=10)

        tk.Label(self.master, text="Student's Mobile no:").grid(row=6, column=0, padx=10, pady=10)
        tk.Entry(self.master, textvariable=self.mobile_var).grid(row=6, column=1, padx=10, pady=10)

        tk.Label(self.master, text="Parent's Mobile no:").grid(row=7, column=0, padx=10, pady=10)
        tk.Entry(self.master, textvariable=self.pmobile_var).grid(row=7, column=1, padx=10, pady=10)

        tk.Label(self.master, text="Email:").grid(row=8, column=0, padx=10, pady=10)
        tk.Entry(self.master, textvariable=self.email_var).grid(row=8, column=1, padx=10, pady=10)

        tk.Button(self.master, text="Add Student", command=self.add_student).grid(row=9, column=0, padx=10, pady=10)
        tk.Button(self.master, text="   Fetch Data   ", command=self.fetch_student).grid(row=0, column=2, padx=10, pady=10)
        tk.Button(self.master, text="Save Updates", command=self.save_updates).grid(row=1, column=2, padx=10, pady=10)
        tk.Button(self.master, text="Delete Student", command=self.delete_student).grid(row=9, column=2, padx=10, pady=10)
        tk.Button(self.master, text="Search Student", command=self.search_student).grid(row=9, column=1, padx=10, pady=10)

        tk.Label(self.master, text="!!MINI PROJECT: Student Management System!!").grid(row=10, column=1, padx=10, pady=0)

    def add_student(self):
        try:
            data = (
                self.roll_no_var.get(),
                self.name_var.get(),
                self.gender_var.get(),
                self.cgpa_var.get(),
                self.semester_var.get(),
                self.dob_var.get(),
                self.mobile_var.get(),
                self.pmobile_var.get(),
                self.email_var.get(),
            )
            if any(not field for field in data):
                messagebox.showerror("Error", "All fields are required!")
                return

            with open(self.file_name, "a") as file:
                file.write(",".join(data) + "\n")
            messagebox.showinfo("Success", f"Student {data[0]} added successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def fetch_student(self):
        """Fetch details of a student by USN and populate fields."""
        try:
            roll_no = self.roll_no_var.get()
            if not roll_no:
                messagebox.showerror("Error", "Enter a USN to fetch!")
                return

            with open(self.file_name, "r") as file:
                for line in file:
                    if line.startswith(roll_no + ","):
                        data = line.strip().split(",")
                        self.name_var.set(data[1])
                        self.gender_var.set(data[2])
                        self.cgpa_var.set(data[3])
                        self.semester_var.set(data[4])
                        self.dob_var.set(data[5])
                        self.mobile_var.set(data[6])
                        self.pmobile_var.set(data[7])
                        self.email_var.set(data[8])
                        messagebox.showinfo("Success", "Student details fetched!! Edit and save updates.")
                        return

            messagebox.showerror("Error", "USN not found!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

#Save Update 
    def save_updates(self):
        try:
            roll_no = self.roll_no_var.get()
            if not roll_no:
                messagebox.showerror("Error", "First Fetch and edit details to save updates!")
                return

            with open(self.file_name, "r") as file:
                lines = file.readlines()

            for i, line in enumerate(lines):
                if line.startswith(roll_no + ","):
                    lines[i] = ",".join(
                        [
                            roll_no,
                            self.name_var.get(),
                            self.gender_var.get(),
                            self.cgpa_var.get(),
                            self.semester_var.get(),
                            self.dob_var.get(),
                            self.mobile_var.get(),
                            self.pmobile_var.get(),
                            self.email_var.get(),
                        ]
                    ) + "\n"
                    break
            else:
                messagebox.showerror("Error", "USN not found!")
                return

            with open(self.file_name, "w") as file:
                file.writelines(lines)
            messagebox.showinfo("Success", "Student details updated successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def delete_student(self):
        try:
            roll_no = simpledialog.askstring("Delete Student", "Enter USN to delete:")
            if not roll_no:
                return

            with open(self.file_name, "r") as file:
                lines = file.readlines()

            with open(self.file_name, "w") as file:
                for line in lines:
                    if not line.startswith(roll_no + ","):
                        file.write(line)
                    else:
                        messagebox.showinfo("Success", f"Student {roll_no} deleted successfully.")
                        return

            messagebox.showerror("Error", "USN not found!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def search_student(self):
        try:
            roll_no = simpledialog.askstring("Search Student", "Enter USN to search:")
            if not roll_no:
                return

            with open(self.file_name, "r") as file:
                for line in file:
                    if line.startswith(roll_no + ","):
                        data = line.strip().split(",")
                        messagebox.showinfo(
                            "Student Data",
                            f"USN: {data[0]}\nName: {data[1]}\nGender: {data[2]}\nCGPA: {data[3]}\nSemester: {data[4]}"
                            f"\nDOB: {data[5]}\nStudent's Mobile: {data[6]}\nParent's Mobile: {data[7]}\nEmail: {data[8]}",
                        )
                        return

            messagebox.showerror("Error", "USN not found!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")


if __name__ == "__main__":
    root = tk.Tk()
    app = StudentManagementSystem(root)
    root.mainloop()
