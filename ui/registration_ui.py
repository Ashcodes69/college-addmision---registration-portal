import tkinter as tk
from tkinter import ttk, messagebox

from services.registration_ser import register_student


class RegistrationUI:
    def __init__(self, root, registration_number=None):  
        self.root = root
        self.root.title("Semester Registration")
        self.root.geometry("500x600")

        ttk.Label(root, text="Semester Registration", font=("Arial", 16)).pack(pady=10)

        self.reg_no = tk.StringVar()
        
        if registration_number:
            self.reg_no.set(registration_number)

        self.sem = tk.StringVar()
        self.major1 = tk.StringVar()
        self.major2 = tk.StringVar()
        self.minor = tk.StringVar()
        self.lang = tk.StringVar()
        self.mdc = tk.StringVar()

        ttk.Label(root, text="Registration Number").pack()
        reg_entry = ttk.Entry(root, textvariable=self.reg_no)
        reg_entry.pack(pady=5)
        
        if registration_number:
            reg_entry.config(state="readonly")

        ttk.Label(root, text="Semester").pack()
        ttk.Entry(root, textvariable=self.sem).pack(pady=5)

        ttk.Label(root, text="Major Paper 1").pack()
        ttk.Entry(root, textvariable=self.major1).pack(pady=5)

        ttk.Label(root, text="Major Paper 2").pack()
        ttk.Entry(root, textvariable=self.major2).pack(pady=5)

        ttk.Label(root, text="Minor Paper").pack()
        ttk.Entry(root, textvariable=self.minor).pack(pady=5)

        ttk.Label(root, text="Language Paper").pack()
        ttk.Entry(root, textvariable=self.lang).pack(pady=5)

        ttk.Label(root, text="MDC Paper").pack()
        ttk.Entry(root, textvariable=self.mdc).pack(pady=5)

        ttk.Button(root, text="Submit Registration", command=self.submit).pack(pady=20)

    def submit(self):
        try:
            data = {
                "semester": self.sem.get(),  
                "registration_number": self.reg_no.get(),
                "Major_paper_1": self.major1.get(),      
                "Major_paper_2": self.major2.get(),     
                "Minor_paper": self.minor.get(),         
                "Language_paper": self.lang.get(),       
                "MDC_paper": self.mdc.get(),            
            }

            result = register_student(data)

            messagebox.showinfo("Success", result)
            
            self.sem.set("")
            self.major1.set("")
            self.major2.set("")
            self.minor.set("")
            self.lang.set("")
            self.mdc.set("")

        except Exception as e:
            messagebox.showerror("Error", str(e))