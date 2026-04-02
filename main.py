import tkinter as tk
from tkinter import messagebox
import subprocess
import sys
import os


def open_login(file_name):
    login_file = os.path.join(os.getcwd(), file_name)
    if os.path.exists(login_file):
        subprocess.Popen([sys.executable, login_file])
    else:
        messagebox.showerror("Error", f"{file_name} not found!")


root = tk.Tk()
root.title("Student Management System")


root.geometry("900x600")
root.resizable(False, False)
root.configure(bg="#2C3E50")



tk.Label(
    root,
    text="Student Management System",
    font=("Arial", 36, "bold"),
    bg="#2C3E50",
    fg="#ECF0F1"
).pack(pady=50)



tk.Label(
    root,
    text="Manage students, teachers, lessons and absences efficiently",
    font=("Arial", 18),
    bg="#2C3E50",
    fg="#BDC3C7",
    wraplength=700,
    justify="center"
).pack(pady=30)



tk.Button(
    root,
    text="Login as Admin",
    font=("Arial", 20, "bold"),
    bg="#E74C3C",
    fg="white",
    width=20,
    height=2,
    command=lambda: open_login("admin/AdminLogin.py")
).pack(pady=15)



tk.Button(
    root,
    text="Login as Student",
    font=("Arial", 20, "bold"),
    bg="#3498DB",
    fg="white",
    width=20,
    height=2,
    command=lambda: open_login("student/StudentLogin.py")
).pack(pady=15)



tk.Button(
    root,
    text="Login as Teacher",
    font=("Arial", 20, "bold"),
    bg="#2ECC71",
    fg="white",
    width=20,
    height=2,
    command=lambda: open_login("teacher/TeacherLogin.py")
).pack(pady=15)


root.mainloop()