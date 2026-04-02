import tkinter as tk
from tkinter import ttk
import os
import sys

src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))


if src_path not in sys.path:
    sys.path.insert(0, src_path)

from connect import create_connection


student_year = 3  


db = create_connection()
if db:
    cursor = db.cursor()
    cursor.execute("""
        SELECT day, time_slot, subject
        FROM schedule
        WHERE year = %s
        ORDER BY FIELD(day,'Sunday','Monday','Tuesday','Wednesday','Thursday'),
                 time_slot
    """, (student_year,))

    rows = cursor.fetchall()
    db.close() 
else:
    rows = [] 
    print("Failed to connect to the database.")


root = tk.Tk()
root.title("Weekly Schedule")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}")

title = tk.Label(
    root,
    text=f"📘 Weekly Schedule - Year {student_year}",
    font=("Arial", 26, "bold")
)
title.pack(pady=20)

style = ttk.Style()
style.configure("Treeview", font=("Arial", 14), rowheight=36)
style.configure("Treeview.Heading", font=("Arial", 16, "bold"))

tree = ttk.Treeview(
    root,
    columns=("Day", "Time", "Subject"),
    show="headings"
)

tree.heading("Day", text="Day")
tree.heading("Time", text="Time")
tree.heading("Subject", text="Subject")

tree.column("Day", width=250, anchor="center")
tree.column("Time", width=300, anchor="center")
tree.column("Subject", width=250, anchor="center")

tree.pack(fill="both", expand=True, padx=40, pady=20)

for row in rows:
    tree.insert("", "end", values=row)

root.mainloop()