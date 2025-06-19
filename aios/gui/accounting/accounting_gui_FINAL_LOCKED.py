# -*- Standards Compliance Declaration -*-
# File: accounting_gui.py
# Purpose: AIOS GUI for manual accounting entry and CSV export
# Standards:
#   - ISO/IEC 27001 (Information Security Management)
#   - ISO/IEC 12207 (Software Lifecycle Processes)
#   - GAAP (Nonprofit Accounting Logic)
#   - WCAG 2.1 AA (Accessibility)
#   - ABL_Rev2_6_1_25 (EI Internal Development Protocol)
#   - IRS Publication 1075 (Taxpayer Data Confidentiality, if applicable)
# Owner: Adaptive Bespoke Learning – Accounting Module Team
# Last Updated: 2025-06-02

"""
This file is FINAL_LOCKED unless reopened with written permission.
All features within this script must align with ABL training modules,
and data entry processes must reflect RAAO's established policy and procedural controls.
"""

import tkinter as tk
from tkinter import messagebox, filedialog
import csv
import datetime

class AccountingGUI:
    def __init__(self, master):
        self.master = master
        master.title("AIOS Manual Accounting Entry")

        # Form Labels and Fields
        self.fields = ["Date", "Vendor", "Amount", "Category", "Description"]
        self.entries = {}

        for idx, field in enumerate(self.fields):
            label = tk.Label(master, text=field)
            label.grid(row=idx, column=0, padx=10, pady=5, sticky="e")

            entry = tk.Entry(master, width=40)
            entry.grid(row=idx, column=1, padx=10, pady=5)
            self.entries[field] = entry

        # Submit Button
        self.submit_btn = tk.Button(master, text="Submit Entry", command=self.submit_entry)
        self.submit_btn.grid(row=len(self.fields), column=0, pady=10)

        # Export Button
        self.export_btn = tk.Button(master, text="Export CSV", command=self.export_csv)
        self.export_btn.grid(row=len(self.fields), column=1, pady=10)

        self.records = []

    def submit_entry(self):
        record = {field: self.entries[field].get() for field in self.fields}
        record["Timestamp"] = datetime.datetime.now().isoformat()
        self.records.append(record)

        messagebox.showinfo("Entry Recorded", "Transaction successfully saved.")
        for entry in self.entries.values():
            entry.delete(0, tk.END)

    def export_csv(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".csv",
                                                 filetypes=[("CSV files", "*.csv")])
        if not file_path:
            return

        with open(file_path, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=self.fields + ["Timestamp"])
            writer.writeheader()
            writer.writerows(self.records)

        messagebox.showinfo("Export Complete", f"Data exported to {file_path}")

if __name__ == "__main__":
    root = tk.Tk()
    gui = AccountingGUI(root)
    root.mainloop()
