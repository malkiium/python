import os
import time
import sys
import random
from datetime import datetime

if getattr(sys, 'frozen', False):
    SCRIPT_DIR = os.path.dirname(sys.executable)
else:
    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

PASSWORDS_FILE = os.path.join(SCRIPT_DIR, 'passwords.txt')

def init_file():
    if not os.path.exists(PASSWORDS_FILE):
        with open(PASSWORDS_FILE, 'w') as f:
            f.write("# My Saved Passwords\n")
            f.write("# Account | Password | Date Added\n")
            f.write("-" * 60 + "\n")

def save_password(account, password):
    passwords = {}
    
    if os.path.exists(PASSWORDS_FILE):
        with open(PASSWORDS_FILE, 'r') as f:
            for line in f:
                if line.startswith('#') or line.startswith('-') or not line.strip():
                    continue
                parts = line.strip().split(' | ')
                if len(parts) >= 2:
                    passwords[parts[0]] = (parts[1], parts[2] if len(parts) > 2 else '')
    
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M')
    passwords[account] = (password, timestamp)
    
    with open(PASSWORDS_FILE, 'w') as f:
        f.write("# My Saved Passwords\n")
        f.write("# Account | Password | Date Added\n")
        f.write("-" * 60 + "\n\n")
        for acc, (pwd, date) in sorted(passwords.items()):
            f.write(f"{acc} | {pwd} | {date}\n")
    
    print(f"✓ Saved password for '{account}'")

def list_passwords():
    passwords = []
    if os.path.exists(PASSWORDS_FILE):
        with open(PASSWORDS_FILE, 'r') as f:
            for line in f:
                if line.startswith('#') or line.startswith('-') or not line.strip():
                    continue
                parts = line.strip().split(' | ')
                if len(parts) >= 2:
                    passwords.append({
                        'account': parts[0],
                        'password': parts[1],
                        'date': parts[2] if len(parts) > 2 else 'Unknown'
                    })
    return passwords

def get_password(account):
    if os.path.exists(PASSWORDS_FILE):
        with open(PASSWORDS_FILE, 'r') as f:
            for line in f:
                if line.startswith('#') or line.startswith('-') or not line.strip():
                    continue
                parts = line.strip().split(' | ')
                if len(parts) >= 2 and parts[0] == account:
                    return parts[1]
    return None

def delete_password(account):
    passwords = {}
    
    if os.path.exists(PASSWORDS_FILE):
        with open(PASSWORDS_FILE, 'r') as f:
            for line in f:
                if line.startswith('#') or line.startswith('-') or not line.strip():
                    continue
                parts = line.strip().split(' | ')
                if len(parts) >= 2:
                    passwords[parts[0]] = (parts[1], parts[2] if len(parts) > 2 else '')
    
    if account not in passwords:
        return False
    
    del passwords[account]
    
    with open(PASSWORDS_FILE, 'w') as f:
        f.write("# My Saved Passwords\n")
        f.write("# Account | Password | Date Added\n")
        f.write("-" * 60 + "\n\n")
        for acc, (pwd, date) in sorted(passwords.items()):
            f.write(f"{acc} | {pwd} | {date}\n")
    
    return True

def generate_password(length=16, use_special=True):
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = "0123456789"
    special = "!@#$%^&*-_=+"
    
    all_chars = lowercase + uppercase + digits
    if use_special:
        all_chars += special
    
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits)
    ]
    
    if use_special:
        password.append(random.choice(special))
    
    remaining = length - len(password)
    password.extend(random.choices(all_chars, k=remaining))
    
    random.shuffle(password)
    
    return ''.join(password)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_menu():
    print("\n" + "="*50)
    print("          Password Generator & Manager")
    print("="*50)
    print(f"\nStorage: {PASSWORDS_FILE}\n")
    print("What would you like to do?")
    print("  1. Generate a new password")
    print("  2. View saved passwords")
    print("  3. Find a specific password")
    print("  4. Delete a password")
    print("  5. Exit")
    print()

def pause(seconds=5):
    for i in range(seconds, 0, -1):
        print(f"\rClosing in {i} seconds...", end="", flush=True)
        time.sleep(1)
    print()

def main():
    init_file()
    
    show_menu()
    choice = input("Enter your choice (1-5): ").strip()
    print()
    
    if choice == "2":
        passwords = list_passwords()
        if passwords:
            print("="*50)
            print("YOUR SAVED PASSWORDS")
            print("="*50)
            for p in passwords:
                print(f"\nAccount:  {p['account']}")
                print(f"Password: {p['password']}")
                print(f"Added:    {p['date']}")
            print("\n" + "="*50)
        else:
            print("You don't have any saved passwords yet.")
        pause()
        return
    
    elif choice == "3":
        account = input("Which account?: ").strip()
        if not account:
            print("No account specified.")
            pause()
            return
        
        pwd = get_password(account)
        if pwd:
            print("\n" + "="*50)
            print(f"Account:  {account}")
            print(f"Password: {pwd}")
            print("="*50)
        else:
            print(f"No password found for '{account}'")
        pause()
        return
    
    elif choice == "4":
        account = input("Which account do you want to delete?: ").strip()
        if not account:
            print("No account specified.")
            pause()
            return
        
        pwd = get_password(account)
        if not pwd:
            print(f"No password found for '{account}'")
            pause()
            return
        
        print(f"\nAccount:  {account}")
        print(f"Password: {pwd}")
        confirm = input("\nAre you sure? Type 'yes' to confirm: ").strip().lower()
        
        if confirm == "yes":
            if delete_password(account):
                print(f"\n✓ Deleted password for '{account}'")
            else:
                print(f"\n✗ Something went wrong")
        else:
            print("\nCancelled.")
        pause()
        return
    
    elif choice == "5":
        print("Goodbye!")
        return
    
    elif choice != "1":
        print("Invalid choice.")
        pause()
        return
    
    account = input("What's this password for? (e.g., 'Gmail', 'Bank'): ").strip()
    if not account:
        print("No account specified.")
        pause()
        return
    
    print("\nPassword options:")
    length_input = input("  Length (press Enter for 16): ").strip()
    length = int(length_input) if length_input.isdigit() else 16
    length = max(8, length)
    
    special_input = input("  Include special characters? (y/n, default yes): ").strip().lower()
    use_special = special_input != 'n'
    
    print("\nGenerating password...")
    time.sleep(0.5)
    
    password = generate_password(length, use_special)
    
    print("\n" + "="*50)
    print(f"YOUR NEW PASSWORD: {password}")
    print("="*50)
    print(f"\nLength: {len(password)} characters")
    
    save = input("\nSave this password? (y/n): ").strip().lower()
    if save == 'y':
        save_password(account, password)
    
    print("\nDone!")
    pause()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nCancelled by user.")
    except Exception as e:
        print(f"\nError: {e}")
        pause(10)