import os
import datetime

# Directory where journal entries are stored
JOURNAL_DIR = r"C:\Users\eliha\vsc\cove\python\journal_entries"
if not os.path.exists(JOURNAL_DIR):
    os.makedirs(JOURNAL_DIR)

def get_filename_for_date(date_str):
    return os.path.join(JOURNAL_DIR, f"journal_{date_str}.txt")

def save_entry():
    entry_text = input("Write your journal entry (Press Enter to save):\n").strip()
    if not entry_text:
        print("No entry text to save.")
        return
    
    current_date_str = datetime.date.today().strftime("%Y-%m-%d")
    filename = get_filename_for_date(current_date_str)
    timestamp = datetime.datetime.now().strftime("%H:%M:%S")
    
    with open(filename, "a", encoding="utf-8") as f:
        f.write(f"----- Entry at {timestamp} -----\n")
        f.write(entry_text + "\n\n")
    
    print("Entry has been saved.")

def view_entries():
    entries = sorted(os.listdir(JOURNAL_DIR))
    if not entries:
        print("No journal entries found.")
        return
    
    for entry in entries:
        if entry.endswith(".txt"):
            date_str = entry.replace("journal_", "").replace(".txt", "")
            with open(get_filename_for_date(date_str), "r", encoding="utf-8") as f:
                content = f.read()
            print(f"Date: {date_str}\n{content}\n{'-' * 40}\n")

def main():
    while True:
        print("\nJournal App")
        print("1. Write a new entry")
        print("2. View all entries")
        print("3. Exit")
        choice = input("Choose an option: ")
        
        if choice == "1":
            print()
            save_entry()
        elif choice == "2":
            print()
            view_entries()
        elif choice == "3":
            print()
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


main()
