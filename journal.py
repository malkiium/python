import tkinter as tk
from tkinter import messagebox
import os
import datetime

# Directory where journal entries are stored
JOURNAL_DIR = "journal_entries"
if not os.path.exists(JOURNAL_DIR):
    os.makedirs(JOURNAL_DIR)

def get_filename_for_date(date_str):
    return os.path.join(JOURNAL_DIR, f"journal_{date_str}.txt")

# Define dark mode colors
BG_COLOR = "#2e2e2e"          # Main window background
TEXT_BG_COLOR = "#333333"     # Text area background
FG_COLOR = "white"            # Text color for labels and text areas
BUTTON_BG_COLOR = "#444444"   # Button background color
BUTTON_FG_COLOR = "white"     # Button text color

class JournalApp:
    def __init__(self, master):
        self.master = master
        master.title("Daily Journal App")
        master.configure(bg=BG_COLOR)
        
        # Set main window geometry to 1000x500 (2:1 ratio)
        master.geometry("1000x500")
        
        self.current_date = datetime.date.today()
        self.current_date_str = self.current_date.strftime("%Y-%m-%d")
        
        # 1) Top Label for Today's Date
        self.date_label = tk.Label(
            master, 
            text=f"Today's Date: {self.current_date_str}",
            bg=BG_COLOR, 
            fg=FG_COLOR, 
            font=("Helvetica", 14)
        )
        self.date_label.pack(pady=10)
        
        # 2) Frame for the Text widget (so it can fill remaining space)
        text_frame = tk.Frame(master, bg=BG_COLOR)
        text_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=(0,10))
        
        # 3) The Text area, which will fill the text_frame
        self.text_area = tk.Text(
            text_frame, 
            bg=TEXT_BG_COLOR, 
            fg=FG_COLOR,
            insertbackground=FG_COLOR,   # cursor color
            highlightbackground="#555555", 
            highlightcolor="#555555"
        )
        self.text_area.pack(fill=tk.BOTH, expand=True)
        
        # 4) Frame for the buttons (placed below the text frame)
        button_frame = tk.Frame(master, bg=BG_COLOR)
        button_frame.pack(pady=5)
        
        # 5) Save button
        self.save_button = tk.Button(
            button_frame, 
            text="Save Entry", 
            command=self.save_entry,
            bg=BUTTON_BG_COLOR, 
            fg=BUTTON_FG_COLOR, 
            activebackground="#555555"
        )
        self.save_button.pack(side=tk.LEFT, padx=5)
        
        # 6) View All Entries button
        self.view_button = tk.Button(
            button_frame, 
            text="View All Journal Entries", 
            command=self.view_entries,
            bg=BUTTON_BG_COLOR, 
            fg=BUTTON_FG_COLOR, 
            activebackground="#555555"
        )
        self.view_button.pack(side=tk.LEFT, padx=5)
        
        # Clear any default text
        self.text_area.delete(1.0, tk.END)
        
        # Check date changes periodically
        self.check_date_change()
        
    def save_entry(self):
        entry_text = self.text_area.get(1.0, tk.END).strip()
        if not entry_text:
            messagebox.showinfo("Info", "No entry text to save.")
            return
        filename = get_filename_for_date(self.current_date_str)
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        # Append the new entry with a timestamp separator
        with open(filename, "a", encoding="utf-8") as f:
            f.write(f"----- Entry at {timestamp} -----\n")
            f.write(entry_text + "\n\n")
        # Clear the text area after saving
        self.text_area.delete(1.0, tk.END)
        messagebox.showinfo("Saved", "Entry has been saved.")
        
    def view_entries(self):
        # Create a new window to display all journal entries in dark mode
        view_win = tk.Toplevel(self.master)
        view_win.title("All Journal Entries")
        view_win.configure(bg=BG_COLOR)
        # Set view window geometry to 1000x500 (2:1 ratio)
        view_win.geometry("1000x500")
        
        # Frame that holds the text widget (to allow it to fill space)
        text_frame = tk.Frame(view_win, bg=BG_COLOR)
        text_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        scrollbar = tk.Scrollbar(text_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        text_widget = tk.Text(
            text_frame, 
            bg=TEXT_BG_COLOR, 
            fg=FG_COLOR,
            insertbackground=FG_COLOR, 
            highlightbackground="#555555", 
            highlightcolor="#555555",
            yscrollcommand=scrollbar.set
        )
        text_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=text_widget.yview)
        
        entries = sorted(os.listdir(JOURNAL_DIR))
        if not entries:
            text_widget.insert(tk.END, "No journal entries found.")
        else:
            for entry in entries:
                if entry.endswith(".txt"):
                    date_str = entry.replace("journal_", "").replace(".txt", "")
                    with open(get_filename_for_date(date_str), "r", encoding="utf-8") as f:
                        content = f.read()
                    text_widget.insert(tk.END, f"Date: {date_str}\n")
                    text_widget.insert(tk.END, content + "\n")
                    text_widget.insert(tk.END, "-" * 40 + "\n")
                    
        text_widget.config(state=tk.DISABLED)
        
    def check_date_change(self):
        # Automatically save and clear the entry area if the system date changes
        new_date = datetime.date.today()
        if new_date != self.current_date:
            if self.text_area.get(1.0, tk.END).strip():
                self.save_entry()
            self.current_date = new_date
            self.current_date_str = new_date.strftime("%Y-%m-%d")
            self.date_label.config(text=f"Today's Date: {self.current_date_str}")
            self.text_area.delete(1.0, tk.END)
        self.master.after(60000, self.check_date_change)

if __name__ == "__main__":
    root = tk.Tk()
    app = JournalApp(root)
    root.mainloop()
