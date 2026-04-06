import tkinter as tk
from tkinter import messagebox

# Create the root window
root = tk.Tk()
root.withdraw()  # Hide the main window

# Show a message box with "hi"
messagebox.showinfo("Greeting", "hi")
