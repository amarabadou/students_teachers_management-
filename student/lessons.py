import tkinter as tk
from tkinter import messagebox
import subprocess
import os
import sys

src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

if src_path not in sys.path:
    sys.path.insert(0, src_path)

from connect import create_connection


BG_DARK = "#0A1929"
FG_LIGHT = "#FFFFFF"
ACCENT_BLUE = "#1565C0"
ACCENT_ORANGE = "#FF9800"

FONT_TITLE = ("Segoe UI", 26, "bold")
FONT_LIST = ("Segoe UI", 14)
FONT_BUTTON = ("Segoe UI", 14, "bold")

class LessonsFromDB:
    def __init__(self, root):
        self.root = root
        root.title("📚 Lessons Library")
        root.configure(bg=BG_DARK)

        w = root.winfo_screenwidth()
        h = root.winfo_screenheight()
        root.geometry(f"{w}x{h}")

        tk.Label(
            root,
            text="📚 Uploaded Lessons",
            font=FONT_TITLE,
            bg=BG_DARK,
            fg=FG_LIGHT
        ).pack(pady=30)

        frame = tk.Frame(root, bg=BG_DARK)
        frame.pack(expand=True, fill="both", padx=120)

        self.listbox = tk.Listbox(
            frame,
            font=FONT_LIST,
            bg="#ECF0F1",
            fg="#2C3E50",
            selectbackground=ACCENT_ORANGE,
            height=15
        )
        self.listbox.pack(side="left", fill="both", expand=True)

        scrollbar = tk.Scrollbar(frame, command=self.listbox.yview)
        scrollbar.pack(side="right", fill="y")
        self.listbox.config(yscrollcommand=scrollbar.set)

        btn_frame = tk.Frame(root, bg=BG_DARK)
        btn_frame.pack(pady=30)

        tk.Button(
            btn_frame,
            text="📂 Open Lesson",
            font=FONT_BUTTON,
            bg=ACCENT_BLUE,
            fg=FG_LIGHT,
            width=18,
            height=2,
            command=self.open_selected
        ).pack(side="left", padx=15)

        tk.Button(
            btn_frame,
            text="🔄 Refresh",
            font=FONT_BUTTON,
            bg=ACCENT_ORANGE,
            fg=BG_DARK,
            width=18,
            height=2,
            command=self.load_lessons
        ).pack(side="left", padx=15)

        tk.Button(
            btn_frame,
            text="⬅ Back",
            font=FONT_BUTTON,
            bg="#1E3A5F",
            fg=FG_LIGHT,
            width=18,
            height=2,
            command=root.destroy
        ).pack(side="left", padx=15)

        self.lessons = []  
        self.load_lessons()

    def load_lessons(self):
        self.listbox.delete(0, tk.END)
        self.lessons.clear()

        conn = None
        cursor = None
        try:
            
            conn = create_connection() 
            if conn:
                cursor = conn.cursor()
                cursor.execute("""
                    SELECT title, file_path, date_uploaded 
                    FROM lessons 
                    ORDER BY date_uploaded DESC
                """)

                rows = cursor.fetchall()

                if not rows:
                    self.listbox.insert(tk.END, "No lessons found in database.")
                    return

                for title, path, date in rows:
                    display_text = f"{title}   ({date.strftime('%Y-%m-%d')})"
                    self.listbox.insert(tk.END, display_text)
                    self.lessons.append((title, path))
            else:
                messagebox.showerror("Error", "Could not connect to database.")

        except Exception as e:
            messagebox.showerror("Database Error", str(e))

        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    def open_selected(self):
        sel = self.listbox.curselection()
        if not sel:
            messagebox.showwarning("No Selection", "Please select a lesson.")
            return

        index = sel[0]
        if index >= len(self.lessons):
            return

        title, file_path = self.lessons[index]

        if not os.path.exists(file_path):
            messagebox.showerror(
                "File Not Found",
                f"The file does not exist:\n{file_path}"
            )
            return

        try:
            if os.name == "nt":
                os.startfile(file_path)
            elif sys.platform == "darwin":
                subprocess.call(("open", file_path))
            else:
                subprocess.call(("xdg-open", file_path))
        except Exception as e:
            messagebox.showerror("Open Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = LessonsFromDB(root)
    root.mainloop()