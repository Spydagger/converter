import tkinter as tk
from tkinter import filedialog, messagebox
import converter
import os

class PDFConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Offline PDF Converter")
        self.root.geometry("400x300")

        # Label
        self.label = tk.Label(root, text="Select files to convert", font=("Arial", 14))
        self.label.pack(pady=20)

        # Buttons
        self.btn_images = tk.Button(root, text="Convert Images to PDF", command=self.convert_images, width=25)
        self.btn_images.pack(pady=10)

        self.btn_text = tk.Button(root, text="Convert Text to PDF", command=self.convert_text, width=25)
        self.btn_text.pack(pady=10)

        # Status
        self.status = tk.Label(root, text="Ready", fg="gray")
        self.status.pack(side=tk.BOTTOM, pady=10)

    def convert_images(self):
        filepaths = filedialog.askopenfilenames(
            title="Select Images",
            filetypes=[("Image Files", "*.jpg *.jpeg *.png *.bmp")]
        )
        if not filepaths:
            return

        save_path = filedialog.asksaveasfilename(
            defaultextension=".pdf",
            filetypes=[("PDF files", "*.pdf")]
        )
        if not save_path:
            return

        success, msg = converter.images_to_pdf(list(filepaths), save_path)
        self.update_status(msg, success)

    def convert_text(self):
        filepath = filedialog.askopenfilename(
            title="Select Text File",
            filetypes=[("Text Files", "*.txt")]
        )
        if not filepath:
            return

        save_path = filedialog.asksaveasfilename(
            defaultextension=".pdf",
            filetypes=[("PDF files", "*.pdf")]
        )
        if not save_path:
            return

        success, msg = converter.text_to_pdf(filepath, save_path)
        self.update_status(msg, success)

    def update_status(self, message, success):
        self.status.config(text=message, fg="green" if success else "red")
        if success:
            messagebox.showinfo("Success", message)
        else:
            messagebox.showerror("Error", message)

if __name__ == "__main__":
    root = tk.Tk()
    app = PDFConverterApp(root)
    root.mainloop()
