import tkinter as tk
from pathlib import Path

import polars as pl
import sv_ttk

root = tk.Tk()
entry = tk.Entry(root, width=30, font=("Arial", 24))
entry.pack()
root.title("Michigan only extractor")


def close_window():
    root.destroy()

def pl_lazy_load():
    selected_index = listbox_files.curselection()

    if selected_index:
        idx = selected_index[0]
        selected_val = listbox_files.get(idx)
        output_string_var.set(f"selected item: {selected_val}")
        print(f"selected item: {selected_val}")
    else:
        output_string_var.set("No selected items")
        return

    output_string_var.set("beginning extraction now")
    file_output_name = "mi_filter_npidata_tkinter.csv"
    q1 = pl.scan_csv(selected_val).filter(
        pl.col("Provider Business Practice Location Address State Name") == "MI"
    )
    pldf = q1.collect()
    pldf.write_csv(file_output_name)

    output_string_var.set(
        f"File successfully extracted to {file_output_name}. Thank you for your patience"
    )
    root.after(4000, close_window)


cwd = Path.cwd()
files_in_current_directory = [
    item.name for item in cwd.iterdir() if item.is_file() and item.suffix == ".csv"
]
listbox_files = tk.Listbox(selectmode=tk.SINGLE, width=80)
listbox_files.pack(pady=10)
for csv in files_in_current_directory:
    listbox_files.insert(tk.END, csv)


select_button = tk.Button(root, text="Start extraction", command=pl_lazy_load)
select_button.pack()

# logger system
output_string_var = tk.StringVar()
output_string_var.set("Please select a file and click the 'Start Extraction' button")

output_label = tk.Label(root, textvariable=output_string_var)
output_label.pack(pady=10)


# This is where the magic happens
sv_ttk.set_theme("dark")

root.mainloop()
