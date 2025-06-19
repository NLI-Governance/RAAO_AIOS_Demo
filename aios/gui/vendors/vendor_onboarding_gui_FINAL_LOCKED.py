# Standards: UI/UX must follow EI/ABL usability practices and include info buttons for each field.
# Validation must reflect IRS, state, and nonprofit procurement rules for tax exemption and vendor verification.

import tkinter as tk
from tkinter import messagebox

def submit_vendor():
    name = name_entry.get()
    ein = ein_entry.get()
    tax_exempt_status = tax_var.get()
    tax_number = tax_number_entry.get()
    terms = payment_terms_entry.get()

    if tax_exempt_status == "yes" and not tax_number:
        messagebox.showerror("Validation Error", "Tax Exempt Number is required.")
        return

    if not name or not ein or (tax_exempt_status == "yes" and not tax_number):
        messagebox.showerror("Validation Error", "Please complete all required fields.")
        return

    messagebox.showinfo("Success", "Vendor information submitted successfully.")

def update_tax_exempt_fields():
    if tax_var.get() == "yes":
        tax_number_label.grid(row=3, column=0, sticky='e')
        tax_number_entry.grid(row=3, column=1)
    else:
        tax_number_label.grid_remove()
        tax_number_entry.grid_remove()

root = tk.Tk()
root.title("Vendor Onboarding")

# Vendor Name
tk.Label(root, text="Vendor Name").grid(row=0, column=0, sticky='e')
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)
tk.Button(root, text="i", command=lambda: messagebox.showinfo("Info", "Enter the full legal name of the vendor.")).grid(row=0, column=2)

# EIN Number
tk.Label(root, text="EIN Number").grid(row=1, column=0, sticky='e')
ein_entry = tk.Entry(root)
ein_entry.grid(row=1, column=1)
tk.Button(root, text="i", command=lambda: messagebox.showinfo("Info", "Employer Identification Number (Federal Tax ID).")).grid(row=1, column=2)

# Tax Exempt Status
tk.Label(root, text="Tax Exempt?").grid(row=2, column=0, sticky='e')
tax_var = tk.StringVar(value="no")
tk.Radiobutton(root, text="Yes", variable=tax_var, value="yes", command=update_tax_exempt_fields).grid(row=2, column=1, sticky='w')
tk.Radiobutton(root, text="No", variable=tax_var, value="no", command=update_tax_exempt_fields).grid(row=2, column=1, sticky='e')
tk.Button(root, text="i", command=lambda: messagebox.showinfo("Info", "Select 'Yes' if the vendor claims tax exemption. A tax exempt number is required.")).grid(row=2, column=2)

# Tax Exempt Number (optional visibility)
tax_number_label = tk.Label(root, text="Tax Exempt Number")
tax_number_entry = tk.Entry(root)

# Payment Terms
tk.Label(root, text="Payment Terms").grid(row=4, column=0, sticky='e')
payment_terms_entry = tk.Entry(root)
payment_terms_entry.grid(row=4, column=1)
tk.Button(root, text="i", command=lambda: messagebox.showinfo("Info", "Enter payment terms (e.g., Net 30, Due on receipt).")).grid(row=4, column=2)

# Submit Button
tk.Button(root, text="Submit", command=submit_vendor).grid(row=5, column=1)

root.mainloop()
