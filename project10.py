import tkinter as tk
from tkinter import filedialog, messagebox
from PyPDF2 import PdfMerger, PdfReader, PdfWriter
import os

def merge_pdfs():
    files = filedialog.askopenfilenames(title="Select PDFs to Merge", filetypes=[("PDF Files", "*.pdf")])
    if not files:
        return

    output_path = filedialog.asksaveasfilename(defaultextension=".pdf", title="Save Merged PDF As", filetypes=[("PDF Files", "*.pdf")])
    if not output_path:
        return

    try:
        merger = PdfMerger()
        for pdf in files:
            merger.append(pdf)
        merger.write(output_path)
        merger.close()
        messagebox.showinfo("Success", f"Merged PDF saved at:\n{output_path}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to merge PDFs.\n{e}")

def split_pdf():
    file = filedialog.askopenfilename(title="Select PDF to Split", filetypes=[("PDF Files", "*.pdf")])
    if not file:
        return

    output_folder = filedialog.askdirectory(title="Select Folder to Save Split PDFs")
    if not output_folder:
        return

    try:
        reader = PdfReader(file)
        for i, page in enumerate(reader.pages):
            writer = PdfWriter()
            writer.add_page(page)
            output_path = os.path.join(output_folder, f"{os.path.splitext(os.path.basename(file))[0]}_page_{i+1}.pdf")
            with open(output_path, "wb") as f:
                writer.write(f)
        messagebox.showinfo("Success", f"PDF split into {len(reader.pages)} pages at:\n{output_folder}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to split PDF.\n{e}")

# GUI Setup
root = tk.Tk()
root.title("PDF Merger & Splitter - Day 10")
root.geometry("500x250")
root.resizable(False, False)
root.config(bg="#111")

title_label = tk.Label(root, text="PDF Merger & Splitter", font=("Poppins", 16, "bold"), bg="#111", fg="#1DB954")
title_label.pack(pady=15)

merge_btn = tk.Button(root, text="Merge PDFs", font=("Poppins", 12, "bold"), bg="#1DB954", fg="black",
                      relief="flat", padx=20, pady=10, command=merge_pdfs)
merge_btn.pack(pady=10)

split_btn = tk.Button(root, text="Split PDF", font=("Poppins", 12, "bold"), bg="#1DB954", fg="black",
                      relief="flat", padx=20, pady=10, command=split_pdf)
split_btn.pack(pady=10)

footer = tk.Label(root, text="Day 10 of 30-Day Coding Challenge | Aryan Sunil & Swara Gharat", 
                  font=("Poppins", 9), bg="#111", fg="gray")
footer.pack(side="bottom", pady=5)

root.mainloop()
