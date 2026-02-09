import tkinter as tk
from tkinter import ttk

from ui.addmision_ui import AdmissionUI
from ui.login_ui import LoginUI
from ui.registration_ui import RegistrationUI


class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("College Admission Portal")
        self.root.geometry("500x400")

        ttk.Label(root, text="College Portal", font=("Arial", 18)).pack(pady=20)

        ttk.Button(root, text="Admission Panel", command=self.open_admission).pack(
            pady=10
        )
        ttk.Button(root, text="Student Login", command=self.open_login).pack(pady=10)
        ttk.Button(
            root, text="Semester Registration", command=self.open_registration
        ).pack(pady=10)

    def open_admission(self):
        win = tk.Toplevel(self.root)
        AdmissionUI(win)

    def open_login(self):
        win = tk.Toplevel(self.root)
        LoginUI(win)

    def open_registration(self):
        win = tk.Toplevel(self.root)
        RegistrationUI(win)


if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()
