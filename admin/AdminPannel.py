import tkinter as tk
from tkinter import ttk, messagebox
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

if src_path not in sys.path:
    sys.path.append(src_path)
from connect import create_connection

BG_DARK = "#34495E"
FG_LIGHT = "white"
ACCENT_GREEN = "#E67E22"
ACCENT_RED = "lightblue"
FONT_TITLE = ('Helvetica', 12, 'bold')
FONT_BODY = ('Helvetica', 10)


class AdminApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Admin Panel")
        self.root.geometry("950x550")
        self.root.configure(bg=BG_DARK)

        self.mode = "students"

        
        self.top_frame = tk.Frame(self.root, bg=BG_DARK)
        self.top_frame.pack(fill="x", pady=10)

        self.form_frame = tk.LabelFrame(self.root, text="Information Form", padx=10, pady=10,
                                        bg=BG_DARK, fg=FG_LIGHT, font=FONT_TITLE)
        self.form_frame.pack(fill="x", padx=10, pady=5)

        self.table_frame = tk.Frame(self.root, bg=BG_DARK)
        self.table_frame.pack(expand=True, fill="both", padx=10, pady=5)

        self.create_top_buttons()
        self.create_form()
        self.show_table()

    
    def create_top_buttons(self):
        btn_style = {"bg": ACCENT_GREEN, "fg": FG_LIGHT, "font": FONT_BODY, "width": 15, "bd": 0,
                     "activebackground": ACCENT_RED, "activeforeground": FG_LIGHT}
        tk.Button(self.top_frame, text="Students", command=lambda: self.switch_mode("students"), **btn_style).pack(
            side=tk.LEFT, padx=10)
        tk.Button(self.top_frame, text="Teachers", command=lambda: self.switch_mode("teachers"), **btn_style).pack(
            side=tk.LEFT, padx=10)

    def switch_mode(self, mode):
        self.mode = mode
       
        for w in self.form_frame.winfo_children():
            w.destroy()
        for w in self.table_frame.winfo_children():
            w.destroy()
        self.create_form()
        self.show_table()

    
    def create_form(self):
        form = self.form_frame

        
        left = tk.Frame(form, bg=BG_DARK)
        left.grid(row=0, column=0, padx=20, pady=5, sticky="nw")

        tk.Label(left, text="Full Name", bg=BG_DARK, fg=FG_LIGHT, font=FONT_BODY).grid(row=0, column=0, sticky="w",
                                                                                       pady=5)
        self.name_entry = tk.Entry(left, width=30, font=FONT_BODY)
        self.name_entry.grid(row=0, column=1)

        tk.Label(left, text="Email", bg=BG_DARK, fg=FG_LIGHT, font=FONT_BODY).grid(row=1, column=0, sticky="w",
                                                                                    pady=5)
        self.email_entry = tk.Entry(left, width=30, font=FONT_BODY)
        self.email_entry.grid(row=1, column=1)

        if self.mode == "students":
            tk.Label(left, text="Age", bg=BG_DARK, fg=FG_LIGHT, font=FONT_BODY).grid(row=2, column=0, sticky="w",
                                                                                     pady=5)
            self.age_entry = tk.Entry(left, width=30, font=FONT_BODY)
            self.age_entry.grid(row=2, column=1)

        
        right = tk.LabelFrame(form, text="Grade / Year", bg=BG_DARK, fg=FG_LIGHT, font=FONT_TITLE)
        right.grid(row=0, column=1, padx=20, sticky="n")

        self.level_var = tk.IntVar(value=0)
        tk.Radiobutton(right, text="First Year", variable=self.level_var, value=1, bg=BG_DARK, fg=FG_LIGHT,
                       selectcolor=ACCENT_GREEN, font=FONT_BODY).pack(anchor="w", pady=2)
        tk.Radiobutton(right, text="Second Year", variable=self.level_var, value=2, bg=BG_DARK, fg=FG_LIGHT,
                       selectcolor=ACCENT_GREEN, font=FONT_BODY).pack(anchor="w", pady=2)
        tk.Radiobutton(right, text="Third Year", variable=self.level_var, value=3, bg=BG_DARK, fg=FG_LIGHT,
                       selectcolor=ACCENT_GREEN, font=FONT_BODY).pack(anchor="w", pady=2)

        btn_frame = tk.Frame(form, bg=BG_DARK)
        btn_frame.grid(row=1, column=0, columnspan=2, pady=15)

        btn_style = {"bg": ACCENT_GREEN, "fg": FG_LIGHT, "font": FONT_BODY, "width": 15, "bd": 0,
                     "activebackground": ACCENT_RED, "activeforeground": FG_LIGHT}
        if self.mode == "students":
            tk.Button(btn_frame, text="Add Student", command=self.add_student, **btn_style).pack(side=tk.LEFT, padx=10)
            tk.Button(btn_frame, text="Update", command=self.update_student, **btn_style).pack(side=tk.LEFT, padx=10)
            tk.Button(btn_frame, text="Delete", command=self.delete_student, **btn_style).pack(side=tk.LEFT, padx=10)
        elif self.mode == "teachers":
            tk.Button(btn_frame, text="Add Teacher", command=self.add_teacher, **btn_style).pack(side=tk.LEFT, padx=10)
            tk.Button(btn_frame, text="Update", command=self.update_teacher, **btn_style).pack(side=tk.LEFT, padx=10)
            tk.Button(btn_frame, text="Delete", command=self.delete_teacher, **btn_style).pack(side=tk.LEFT, padx=10)

    
    def show_table(self):
        if self.mode == "students":
            columns = ("ID", "Full Name", "Email", "Grade", "Age")
        else:
            columns = ("ID", "Full Name", "Email", "Grade")

        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview", background=BG_DARK, foreground=FG_LIGHT, fieldbackground=BG_DARK,
                        font=FONT_BODY)
        style.configure("Treeview.Heading", font=FONT_TITLE, background=ACCENT_GREEN, foreground=FG_LIGHT)

        self.tree = ttk.Treeview(self.table_frame, columns=columns, show="headings")
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=140, anchor="center")

        self.tree.pack(expand=True, fill="both")
        self.tree.bind("<<TreeviewSelect>>", self.fill_form)

        self.load_data()

    
    def load_data(self):
        self.tree.delete(*self.tree.get_children())
        db = create_connection()
        cursor = db.cursor()

        if self.mode == "students":
            cursor.execute("SELECT student_id, full_name, email, level_id, age FROM students")
        else:
            cursor.execute("SELECT teacher_id, full_name, email, level_id FROM teachers")

        for row in cursor.fetchall():
            self.tree.insert("", tk.END, values=row)

        db.close()

    
    def fill_form(self, event):
        data = self.tree.item(self.tree.focus())["values"]
        if not data:
            return

        self.selected_id = data[0]

        self.name_entry.delete(0, tk.END)
        self.name_entry.insert(0, data[1])

        self.email_entry.delete(0, tk.END)
        self.email_entry.insert(0, data[2])

        self.level_var.set(data[3])

        if self.mode == "students":
            self.age_entry.delete(0, tk.END)
            self.age_entry.insert(0, data[4])

    
    def add_student(self):
        db = create_connection()
        cursor = db.cursor()
        cursor.execute(
            "INSERT INTO students (full_name,email,age,level_id) VALUES (%s,%s,%s,%s)",
            (self.name_entry.get(), self.email_entry.get(),
             self.age_entry.get(), self.level_var.get()))
        db.commit()
        db.close()
        self.load_data()

    def update_student(self):
        if not hasattr(self, "selected_id"):
            return
        db = create_connection()
        cursor = db.cursor()
        cursor.execute(
            "UPDATE students SET full_name=%s,email=%s,age=%s,level_id=%s WHERE student_id=%s",
            (self.name_entry.get(), self.email_entry.get(),
             self.age_entry.get(), self.level_var.get(), self.selected_id))
        db.commit()
        db.close()
        self.load_data()

    def delete_student(self):
        if not hasattr(self, "selected_id"):
            return
        db = create_connection()
        cursor = db.cursor()
        cursor.execute("DELETE FROM students WHERE student_id=%s", (self.selected_id,))
        db.commit()
        db.close()
        self.load_data()

    #
    def add_teacher(self):
        db = create_connection()
        cursor = db.cursor()
        cursor.execute(
            "INSERT INTO teachers (full_name,email,level_id) VALUES (%s,%s,%s)",
            (self.name_entry.get(), self.email_entry.get(), self.level_var.get()))
        db.commit()
        db.close()
        self.load_data()

    def update_teacher(self):
        if not hasattr(self, "selected_id"):
            return
        db = create_connection()
        cursor = db.cursor()
        cursor.execute(
            "UPDATE teachers SET full_name=%s,email=%s,level_id=%s WHERE teacher_id=%s",
            (self.name_entry.get(), self.email_entry.get(),
             self.level_var.get(), self.selected_id))
        db.commit()
        db.close()
        self.load_data()

    def delete_teacher(self):
        if not hasattr(self, "selected_id"):
            return
        db = create_connection()
        cursor = db.cursor()
        cursor.execute("DELETE FROM teachers WHERE teacher_id=%s", (self.selected_id,))
        db.commit()
        db.close()
        self.load_data()


if __name__ == "__main__":
    root = tk.Tk()
    AdminApp(root)
    root.mainloop()
