import tkinter as tk
from tkinter import messagebox
import os
import sys
import subprocess
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))


if src_path not in sys.path:
    sys.path.append(src_path)


from connect import create_connection

def login_admin():
    username = username_entry.get()
    password = password_entry.get()

    conn = create_connection() 
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM admins WHERE username=%s AND password=%s", (username, password))
        result = cursor.fetchone()
        
        if result:
            
            admin_file = os.path.join(os.path.dirname(__file__), "AdminPannel.py")
            subprocess.Popen([sys.executable, admin_file])
            root.destroy()
        else:
            messagebox.showerror("Error", "Incorrect username or password!")
        
        cursor.close()
        conn.close()


root = tk.Tk()
root.title("Admin Login")


root.geometry("900x600")
root.resizable(False, False)
root.configure(bg="#34495E")



tk.Label(
    root,
    text="Admin Login",
    font=("Arial", 28, "bold"),
    bg="#34495E",
    fg="white"
).pack(pady=40)



tk.Label(
    root,
    text="Username:",
    font=("Arial", 18),
    bg="#34495E",
    fg="white"
).pack(pady=10)
username_entry = tk.Entry(root, font=("Arial", 16), width=30)
username_entry.pack(pady=5)



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
    bg="#E67E22",
    fg="white",
    width=25,
    height=2,
    command=login_admin
).pack(pady=30)


root.mainloop()