import tkinter as tk
from register import register
from login import login

def open_register():
    register()

def open_login():
    login()

root = tk.Tk()
root.title("Graphical Password Authentication")
root.geometry("400x300")
root.configure(bg="#1e1e2f")
root.iconbitmap(r"C:\Users\Y BUNNY\OneDrive\Desktop\GPA-GUI\icon.ico")

title = tk.Label(root, text="Graphical Password System",
                 font=("Arial", 16, "bold"),
                 bg="#1e1e2f", fg="white")
title.pack(pady=30)

btn_register = tk.Button(root, text="Register",
                         command=open_register,
                         width=20, height=2,
                         bg="#4CAF50", fg="white")
btn_register.pack(pady=10)

btn_login = tk.Button(root, text="Login",
                      command=open_login,
                      width=20, height=2,
                      bg="#2196F3", fg="white")
btn_login.pack(pady=10)

btn_exit = tk.Button(root, text="Exit",
                     command=root.destroy,
                     width=20, height=2,
                     bg="#f44336", fg="white")
btn_exit.pack(pady=10)

root.mainloop()