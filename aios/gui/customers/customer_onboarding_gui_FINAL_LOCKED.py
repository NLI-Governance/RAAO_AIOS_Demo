# ~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/aios/gui/customers/customer_onboarding_gui.py
# Standards: IRS Pub 557, ISO 20022, NACHA, ADA Title III

import tkinter as tk
from tkinter import messagebox

def submit_form():
    name = name_entry.get()
    ein = ein_entry.get()
    tax_exempt = tax_exempt_var.get()
    tax_exempt_number = tax_exempt_number_entry.get()

    if not name or not ein:
        messagebox.showerror("Missing Info", "Customer name and EIN are required.")
        return

    if tax_exempt == "Yes" and not tax_exempt_number:
        messagebox.showerror("Missing Info", "Tax Exempt Number is required when tax exempt is 'Yes'.")
        return

    # Here you would save to a .csv or database
    print(f"Name: {name}, EIN: {ein}, Tax Exempt: {tax_exempt}, Tax Exempt Number: {tax_exempt_number}")
    messagebox.showinfo("Success", "Customer onboarded successfully.")

def toggle_tax_number(*args):
    if tax_exempt_var.get() == "Yes":
        tax_exempt_number_label.grid(row=3, column=0, sticky="e")
        tax_exempt_number_entry.grid(row=3, column=1)
    else:
        tax_exempt_number_label.grid_forget()
        tax_exempt_number_entry.grid_forget()

# GUI Setup
root = tk.Tk()
root.title("Customer Onboarding")

tk.Label(root, text="Customer Name").grid(row=0, column=0, sticky="e")
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)

tk.Label(root, text="EIN").grid(row=1, column=0, sticky="e")
ein_entry = tk.Entry(root)
ein_entry.grid(row=1, column=1)

tk.Label(root, text="Tax Exempt?").grid(row=2, column=0, sticky="e")
tax_exempt_var = tk.StringVar()
tax_exempt_dropdown = tk.OptionMenu(root, tax_exempt_var, "No", "Yes")
tax_exempt_dropdown.grid(row=2, column=1)
tax_exempt_var.set("No")
tax_exempt_var.trace("w", toggle_tax_number)

tax_exempt_number_label = tk.Label(root, text="Tax Exempt Number")
tax_exempt_number_entry = tk.Entry(root)

tk.Button(root, text="Submit", command=submit_form).grid(row=4, column=0, columnspan=2, pady=10)

root.mainloop()
