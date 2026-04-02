import tkinter as tk
from tkinter import messagebox
import subprocess
import sys
import os


src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if src_path not in sys.path:
    sys.path.insert(0, src_path)


from connect import create_connection

def login_teacher():
    email = email_entry.get()
    password = password_entry.get()

    conn = create_connection() 
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * FROM teachers WHERE email=%s AND password=%s",
                (email, password)
            )
            result = cursor.fetchone()

            if result:
               
                pannel_path = os.path.join(os.path.dirname(__file__), "TeacherPannel.py")
                
                if os.path.exists(pannel_path):
                    subprocess.Popen([sys.executable, pannel_path])
                    root.destroy()
                else:
                    messagebox.showerror("Error", "TeacherPannel.py not found!")
            else:
                messagebox.showerror("Error", "Incorrect email or password!")

            cursor.close()
            conn.close()
        except Exception as e:
            messagebox.showerror("Database Error", str(e))
    else:
       
        pass


root = tk.Tk()
root.title("Teacher Login")
root.geometry("900x600")
root.resizable(False, False)
root.configure(bg="#34495E")

tk.Label(
    root,
    text="Teacher Login",
    font=("Arial", 28, "bold"),
    bg="#34495E",
    fg="white"
).pack(pady=40)

tk.Label(
    root,
    text="Email:",
    font=("Arial", 18),
    bg="#34495E",
    fg="white"
).pack(pady=10)

email_entry = tk.Entry(root, font=("Arial", 16), width=30)
email_entry.pack(pady=5)

tk.Label(
    root,
    text="Password:",
    font=("Arial", 18),
    bg="#34495E",
    fg="white"
).pack(pady=10)

password_entry = tk.Entry(root, font=("Arial", 16), show="*", width=30)
password_entry.pack(pady=5)

tk.Button(
    root,
    text="Login",
    font=("Arial", 18, "bold"),
    bg="#2ECC71",
    fg="white",
    width=25,
    height=2,
    command=login_teacher
).pack(pady=30)

root.mainloop()