import tkinter as tk
from tkinter import filedialog, messagebox
import os
import shutil
import sys
import subprocess

current_dir = os.path.dirname(os.path.abspath(__file__))
src_path = os.path.abspath(os.path.join(current_dir, '..'))

if src_path not in sys.path:
    sys.path.insert(0, src_path)

from connect import create_connection 


UPLOADS_DIRECTORY = os.path.join(src_path, "Uploaded_Lessons")


BG_DARK = "#34495E"      
FG_LIGHT = "white"       
ACCENT_ORANGE = "#E67E22" 
ACCENT_BLUE = "lightblue"   
FONT_TITLE = ('Helvetica', 16, 'bold')
FONT_BODY = ('Helvetica', 10)

class PDFUploaderApp:
    def __init__(self, master):
        self.master = master
        master.title("Lesson Uploader")
        master.config(bg=BG_DARK)
        master.geometry("500x550")
        
        
        tk.Label(
            master, 
            text="📚 Lesson Management", 
            font=("Helvetica", 24, "bold"), 
            bg=BG_DARK, 
            fg=FG_LIGHT
        ).pack(pady=30)

   
        tk.Label(master, text="Lesson Title:", bg=BG_DARK, fg=FG_LIGHT, font=FONT_BODY).pack(pady=(10, 0))
        self.title_entry = tk.Entry(master, width=40, font=FONT_BODY)
        self.title_entry.pack(pady=(5, 10))
        
        id_frame = tk.Frame(master, bg=BG_DARK)
        id_frame.pack(pady=(5, 10))

        
        teacher_frame = tk.Frame(id_frame, bg=BG_DARK)
        teacher_frame.pack(side=tk.LEFT, padx=15)
        tk.Label(teacher_frame, text="Teacher ID:", bg=BG_DARK, fg=FG_LIGHT, font=FONT_BODY).pack()
        self.teacher_id_entry = tk.Entry(teacher_frame, width=10, justify=tk.CENTER)
        self.teacher_id_entry.pack(pady=5)
        
        
        level_frame = tk.Frame(id_frame, bg=BG_DARK)
        level_frame.pack(side=tk.LEFT, padx=15)
        tk.Label(level_frame, text="Level ID:", bg=BG_DARK, fg=FG_LIGHT, font=FONT_BODY).pack()
        self.level_id_entry = tk.Entry(level_frame, width=10, justify=tk.CENTER)
        self.level_id_entry.pack(pady=5)
        
        
        self.path_var = tk.StringVar(value="No file selected.")
        self.path_label = tk.Label(master, textvariable=self.path_var, wraplength=400, bg="#ECF0F1", fg="#2C3E50", font=FONT_BODY, padx=10, pady=10)
        self.path_label.pack(pady=20, padx=40, fill=tk.X)
        
       
        button_frame = tk.Frame(master, bg=BG_DARK)
        button_frame.pack(pady=20)
        
        tk.Button(button_frame, text="Upload PDF", command=self.upload_file, font=FONT_BODY, bg=ACCENT_BLUE, width=15, height=2).pack(side=tk.LEFT, padx=10) 
        tk.Button(button_frame, text="View Lessons", command=self.list_and_open_lessons, font=FONT_BODY, bg=ACCENT_ORANGE, fg=FG_LIGHT, width=15, height=2).pack(side=tk.LEFT, padx=10) 
        
        self.status_var = tk.StringVar()
        tk.Label(master, textvariable=self.status_var, fg="#F1C40F", bg=BG_DARK, font=FONT_BODY).pack(pady=10)

    def upload_file(self):
        title = self.title_entry.get().strip()
        try:
            t_id = int(self.teacher_id_entry.get().strip())
            l_id = int(self.level_id_entry.get().strip())
        except ValueError:
            messagebox.showerror("Input Error", "IDs must be numeric numbers.")
            return

        filepath = filedialog.askopenfilename(filetypes=[("PDF Documents", "*.pdf")])
        if not filepath: return

        self.path_var.set(f"Selected: {os.path.basename(filepath)}")

        conn = create_connection()
        if conn:
            try:
                if not os.path.exists(UPLOADS_DIRECTORY):
                    os.makedirs(UPLOADS_DIRECTORY)
                
                filename = os.path.basename(filepath)
                dest = os.path.join(UPLOADS_DIRECTORY, filename)
                shutil.copy(filepath, dest)
                
                
                db_save_path = os.path.join("Uploaded_Lessons", filename)
                
                cursor = conn.cursor()
                query = "INSERT INTO lessons (title, file_path, teacher_id, level_id) VALUES (%s, %s, %s, %s)"
                cursor.execute(query, (title, db_save_path, t_id, l_id))
                conn.commit()
                messagebox.showinfo("Success", f"Lesson '{title}' uploaded successfully!")
                self.status_var.set("Upload successful.")
            except Exception as e:
                messagebox.showerror("Error", f"Database error: {e}")
            finally:
                conn.close()

    def list_and_open_lessons(self):
        if not os.path.exists(UPLOADS_DIRECTORY):
            messagebox.showinfo("Empty", "No lessons found.")
            return
        files = [f for f in os.listdir(UPLOADS_DIRECTORY) if f.lower().endswith('.pdf')]
        if files:
            self.open_selection_window(files)
        else:
            messagebox.showinfo("Notice", "No PDF files in the uploads folder.")

    def open_selection_window(self, files):
        sw = tk.Toplevel(self.master)
        sw.title("Select Lesson")
        sw.geometry("400x450")
        sw.configure(bg=BG_DARK)

        tk.Label(sw, text="Choose a file to open:", bg=BG_DARK, fg=FG_LIGHT, font=FONT_BODY).pack(pady=10)

        lb = tk.Listbox(sw, width=50, height=15)
        lb.pack(padx=20, pady=10)
        for f in files: lb.insert(tk.END, f)
        
        def open_f():
            try:
                selection = lb.curselection()
                if not selection: return
                fname = lb.get(selection[0])
                fpath = os.path.join(UPLOADS_DIRECTORY, fname)
                
                if os.name == 'nt':
                    os.startfile(fpath)
                else:
                    cmd = 'open' if sys.platform == 'darwin' else 'xdg-open'
                    subprocess.call((cmd, fpath))
            except Exception as e:
                messagebox.showerror("Error", f"Could not open file: {e}")
        
        tk.Button(sw, text="Open Selected File", command=open_f, bg=ACCENT_ORANGE, fg=FG_LIGHT, width=20).pack(pady=10)
        tk.Button(sw, text="Close", command=sw.destroy, bg="gray", fg="white", width=10).pack(pady=5)

if __name__ == '__main__':
    root = tk.Tk()
    app = PDFUploaderApp(root)
    root.mainloop()