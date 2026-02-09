import tkinter as tk
from tkinter import ttk, messagebox

from services.addmision_ser import create_student


class AdmissionUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Admission Form")
        self.root.geometry("900x650")

        ttk.Label(root, text="College Admission Form", font=("Arial", 14, "bold")).pack(pady=10)

        main = ttk.Frame(root, padding="20")
        main.pack(fill="both", expand=True)

        ttk.Label(main, text="Personal Details", font=("Arial", 11, "bold")).grid(row=0, column=0, columnspan=4, sticky="w", pady=(0,10))
        
        row = 1
        self.name = self.add_field(main, "Name", row, 0)
        self.dob = self.add_field(main, "DOB (DD/MM/YYYY)", row, 2)
        
        row += 1
        self.mobile_no = self.add_field(main, "Mobile No", row, 0)
        self.email = self.add_field(main, "Email", row, 2)
        
        row += 1
        self.religion = self.add_field(main, "Religion", row, 0)
        self.category = self.add_dropdown(main, "Category", row, 2, ["General", "OBC", "SC", "ST"])

        row += 1
        ttk.Label(main, text="Address Details", font=("Arial", 11, "bold")).grid(row=row, column=0, columnspan=4, sticky="w", pady=(15,10))
        
        row += 1
        self.address = self.add_field(main, "Address", row, 0)
        self.pinCode = self.add_field(main, "Pin Code", row, 2)
        
        row += 1
        self.ps = self.add_field(main, "Police Station", row, 0)
        self.district = self.add_field(main, "District", row, 2)
        
        row += 1
        self.state = self.add_field(main, "State", row, 0)
        self.nationality = self.add_field(main, "Nationality", row, 2)

        row += 1
        ttk.Label(main, text="Parent Details", font=("Arial", 11, "bold")).grid(row=row, column=0, columnspan=4, sticky="w", pady=(15,10))
        
        row += 1
        self.father_name = self.add_field(main, "Father's Name", row, 0)
        self.father_occupation = self.add_field(main, "Father's Occupation", row, 2)
        
        row += 1
        self.mother_name = self.add_field(main, "Mother's Name", row, 0)
        self.mother_occupation = self.add_field(main, "Mother's Occupation", row, 2)

        row += 1
        ttk.Label(main, text="Academic Details", font=("Arial", 11, "bold")).grid(row=row, column=0, columnspan=4, sticky="w", pady=(15,10))
        
        row += 1
        self.previous_institution = self.add_field(main, "Previous Institution", row, 0)
        self.prev_marks_per = self.add_field(main, "Previous Marks %", row, 2)
        
        row += 1
        self.department = self.add_field(main, "Department", row, 0)

        row += 1
        ttk.Button(main, text="Submit Admission", command=self.submit).grid(row=row, column=0, columnspan=4, pady=20)

    def add_field(self, parent, label_text, row, col):
        ttk.Label(parent, text=label_text, font=("Arial", 9)).grid(row=row, column=col, sticky="w", padx=5, pady=5)
        var = tk.StringVar()
        ttk.Entry(parent, textvariable=var, width=25).grid(row=row, column=col+1, padx=5, pady=5)
        return var

    def add_dropdown(self, parent, label_text, row, col, values):
        ttk.Label(parent, text=label_text, font=("Arial", 9)).grid(row=row, column=col, sticky="w", padx=5, pady=5)
        var = tk.StringVar()
        ttk.Combobox(parent, textvariable=var, values=values, width=23, state="readonly").grid(row=row, column=col+1, padx=5, pady=5)
        return var

    def submit(self):
        try:
            data = {
                "name": self.name.get(),
                "DOB": self.dob.get(),
                "mobile_no": self.mobile_no.get(),
                "email": self.email.get(),
                "religion": self.religion.get(),
                "category": self.category.get(),
                "address": self.address.get(),
                "pinCode": self.pinCode.get(),
                "ps": self.ps.get(),
                "district": self.district.get(),
                "state": self.state.get(),
                "Nationality": self.nationality.get(),
                "father_name": self.father_name.get(),
                "father_occupation": self.father_occupation.get(),
                "mother_name": self.mother_name.get(),
                "mother_occupation": self.mother_occupation.get(),
                "previous_institution": self.previous_institution.get(),
                "prev_marks_per": self.prev_marks_per.get(),
                "department": self.department.get()
            }

            reg_no, roll_no = create_student(data)

            messagebox.showinfo(
                "Success",
                f"Admission Successful!\n\nRegistration No: {reg_no}\nRoll No: {roll_no}"
            )

            for var in [self.name, self.dob, self.mobile_no, self.email, self.religion, 
                       self.category, self.address, self.pinCode, self.ps, self.district, 
                       self.state, self.nationality, self.father_name, self.father_occupation,
                       self.mother_name, self.mother_occupation, self.previous_institution,
                       self.prev_marks_per, self.department]:
                var.set("")

        except Exception as e:
            messagebox.showerror("Error", str(e))