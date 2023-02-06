import tkinter as tk

root = tk.Tk()

root.geometry("640x480")
root.title("PUP QC Attendance Monitoring System")

label = tk.Label(root, text="Hello World!", font=("Fira Code", 15))
label.pack(padx=20, pady=20)

textbox = tk.Text(root, height=3, font=("JetBrains Nerd Font Mono", 11))
textbox.pack()

root.mainloop()