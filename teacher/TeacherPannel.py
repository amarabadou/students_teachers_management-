import tkinter as tk
from tkinter import font
import subprocess
import sys


root = tk.Tk()
root.title("🎓 Teacher Dashboard")
root.configure(bg="#0A1929")


screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}")


title_font = font.Font(family="Segoe UI", size=32, weight="bold")
button_font = font.Font(family="Segoe UI", size=16, weight="bold")
description_font = font.Font(family="Segoe UI", size=12)


header_frame = tk.Frame(root, bg="#0A1929", height=150)
header_frame.pack(fill="x", pady=(0, 30))

title = tk.Label(
    header_frame,
    text="🎓 Teacher Dashboard",
    font=title_font,
    fg="#FFFFFF",
    bg="#0A1929"
)
title.pack(pady=40)

description = tk.Label(
    header_frame,
    text="Your Academic Management Portal",
    font=description_font,
    fg="#4FC3F7",
    bg="#0A1929"
)
description.pack()


main_frame = tk.Frame(root, bg="#0A1929")
main_frame.pack(expand=True)


button_style = {
    "font": button_font,
    "width": 28,
    "height": 2,
    "bd": 0,
    "cursor": "hand2",
    "activebackground": "#FF9800",
}


def open_pdf():
    subprocess.Popen([sys.executable, "teacher/pdf2testf.py"])



btn_pdf = tk.Button(
    main_frame,
    text="📄  PDF",
    **button_style,
    bg="#1565C0",
    fg="#FFFFFF",
    activeforeground="#FFFFFF",
    command=open_pdf
)
btn_pdf.pack(pady=20)


divider = tk.Frame(main_frame, height=2, width=400, bg="#1E3A5F")
divider.pack(pady=10)




footer_frame = tk.Frame(root, bg="#0A1929", height=80)
footer_frame.pack(side="bottom", fill="x", pady=(40, 0))

footer_text = tk.Label(
    footer_frame,
    text="Student Dashboard v2.0 • Modern UI Design",
    font=description_font,
    fg="#546E7A",
    bg="#0A1929"
)
footer_text.pack()


def on_enter(e):
    e.widget['bg'] = '#1976D2' if e.widget == btn_pdf else '#FFB74D'

def on_leave(e):
    e.widget['bg'] = '#1565C0' if e.widget == btn_pdf else '#FF9800'

btn_pdf.bind("<Enter>", on_enter)
btn_pdf.bind("<Leave>", on_leave)



for btn in [btn_pdf]:
    btn.config(
        relief="flat",
        highlightbackground="#1E3A5F",
        highlightcolor="#1E3A5F",
        highlightthickness=2
    )


root.update_idletasks()
x = (screen_width - root.winfo_width()) // 2
y = (screen_height - root.winfo_height()) // 2
root.geometry(f"+{x}+{y}")

root.mainloop()