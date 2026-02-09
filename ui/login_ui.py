import tkinter as tk
from tkinter import ttk, messagebox

from services.auth_ser import set_password, login_student
from ui.registration_ui import RegistrationUI


class LoginUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Login")
        self.root.geometry("500x400")

        ttk.Label(root, text="Student Login", font=("Arial", 16)).pack(pady=10)

        self.reg_no = tk.StringVar()
        self.password = tk.StringVar()

        ttk.Label(root, text="Registration Number").pack()
        ttk.Entry(root, textvariable=self.reg_no).pack(pady=5)

        ttk.Label(root, text="Password").pack()
        ttk.Entry(root, textvariable=self.password, show="*").pack(pady=5)

        ttk.Button(root, text="Login", command=self.login).pack(pady=10)
        ttk.Button(root, text="Set Password (First Time)", command=self.set_pass).pack(pady=10)

    def login(self):
        try:
            reg = self.reg_no.get()
            pwd = self.password.get()

            result = login_student(reg, pwd)

            messagebox.showinfo("Login Success", result)
            
            self.open_registration_ui(reg)

        except Exception as e:
            messagebox.showerror("Login Failed", str(e))

    def set_pass(self):
        try:
            reg = self.reg_no.get()
            pwd = self.password.get()

            result = set_password(reg, pwd)

            messagebox.showinfo("Password Set", result)

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def open_registration_ui(self, reg_no):

        self.root.destroy()
        
        new_root = tk.Tk()
        RegistrationUI(new_root, reg_no)
        new_root.mainloop()