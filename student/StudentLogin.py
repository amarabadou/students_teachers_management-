import tkinter as tk
from tkinter import messagebox
import subprocess
import os
import sys


current_dir = os.path.dirname(os.path.abspath(__file__))


project_root = os.path.dirname(current_dir)


if project_root not in sys.path:
    sys.path.append(project_root)

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from connect import create_connection

def login_student():
    email = email_entry.get()
    password = password_entry.get()

    conn = create_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT student_id FROM students WHERE email=%s AND password=%s", (email, password))
        result = cursor.fetchone()
        
        if result:
            student_id = result[0]
           
            student_file = os.path.join(os.path.dirname(__file__), "StudentPannel.py")
            subprocess.Popen([sys.executable, student_file, str(student_id)])
            root.destroy()
        else:
            messagebox.showerror("Error", "Incorrect email or password!")
        
        cursor.close()
        conn.close()

root = tk.Tk()
root.title("Student Login")
root.geometry("900x600")
root.resizable(False, False)
root.configure(bg="#34495E")

tk.Label(root, text="Student Login", font=("Arial", 28, "bold"),
         bg="#34495E", fg="white").pack(pady=40)

tk.Label(root, text="Email:", font=("Arial", 18),
         bg="#34495E", fg="white").pack(pady=10)
email_entry = tk.Entry(root, font=("Arial", 16), width=30)
email_entry.pack(pady=5)

tk.Label(root, text="Password:", font=("Arial", 18),
         bg="#34495E", fg="white").pack(pady=10)
password_entry = tk.Entry(root, font=("Arial", 16), show="*", width=30)
password_entry.pack(pady=5)

tk.Button(root, text="Login", font=("Arial", 18, "bold"),
          bg="#3498DB", fg="white", width=25, height=2,
          command=login_student).pack(pady=30)

root.mainloop()