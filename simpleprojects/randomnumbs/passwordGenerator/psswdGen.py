import sqlite3
import os

# Get the directory where THIS script is located
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(SCRIPT_DIR, 'passwords.db')

# -------- DATABASE SETUP --------
def init_database():
    """Initialize the SQLite database for storing passwords"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Create table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS passwords (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            use TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    conn.commit()
    conn.close()

def save_password(use, password):
    """Save password to database"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    try:
        cursor.execute('INSERT INTO passwords (use, password) VALUES (?, ?)', (use, password))
        conn.commit()
        print(f"\n✓ Password saved for '{use}'")
    except sqlite3.IntegrityError:
        # If use already exists, update it
        cursor.execute('UPDATE passwords SET password = ?, created_at = CURRENT_TIMESTAMP WHERE use = ?', (password, use))
        conn.commit()
        print(f"\n✓ Password updated for '{use}'")
    
    conn.close()

def list_all_passwords():
    """List all saved password uses"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute('SELECT use, password, created_at FROM passwords ORDER BY created_at DESC')
    results = cursor.fetchall()
    
    conn.close()
    return results

def get_password(use):
    """Retrieve a specific password"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute('SELECT password FROM passwords WHERE use = ?', (use,))
    result = cursor.fetchone()
    
    conn.close()
    return result[0] if result else None

def delete_password(use):
    """Delete a specific password"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute('DELETE FROM passwords WHERE use = ?', (use,))
    deleted = cursor.rowcount > 0
    
    conn.commit()
    conn.close()
    
    return deleted

# -------- INITIALIZE DATABASE --------
init_database()

# -------- USER INTERACTION --------
print("="*60)
print("    CHAOTIC PASSWORD GENERATOR")
print("="*60)
print(f"\nDatabase location: {DB_PATH}")
print("\nOptions:")
print("1. Generate a new password")
print("2. View saved passwords")
print("3. Retrieve a specific password")
print("4. Delete a password")

choice = input("\nChoose an option (1/2/3/4): ").strip()

if choice == "2":
    passwords = list_all_passwords()
    if passwords:
        print("\n" + "="*60)
        print("SAVED PASSWORDS:")
        print("="*60)
        for use, pwd, created in passwords:
            print(f"\nUse: {use}")
            print(f"Password: {pwd}")
            print(f"Created: {created}")
        print("="*60)
    else:
        print("\nNo passwords saved yet.")
    exit()

elif choice == "3":
    use = input("\nWhat is the password for?: ").strip()
    pwd = get_password(use)
    if pwd:
        print(f"\n{'='*60}")
        print(f"Password for '{use}': {pwd}")
        print("="*60)
    else:
        print(f"\nNo password found for '{use}'")
    exit()

elif choice == "4":
    use = input("\nWhat password do you want to delete?: ").strip()
    if not use:
        print("No use specified. Exiting.")
        exit()
    
    # Show the password before deleting
    pwd = get_password(use)
    if not pwd:
        print(f"\nNo password found for '{use}'")
        exit()
    
    print(f"\nPassword for '{use}': {pwd}")
    confirm = input(f"\nAre you sure you want to delete this? (yes/no): ").strip().lower()
    
    if confirm == "yes":
        if delete_password(use):
            print(f"\n✓ Password for '{use}' has been deleted.")
        else:
            print(f"\n✗ Failed to delete password for '{use}'")
    else:
        print("\nDeletion cancelled.")
    exit()

elif choice != "1":
    print("\nInvalid choice. Exiting.")
    exit()

# If choice is 1, continue with password generation
password_use = input("\nWhat is this password for?: ").strip()
if not password_use:
    print("No use specified. Exiting.")
    exit()

print("\nGenerating your password...\n")

# -------- CHAOS SEED BUILDER -------- 
def build_seed():
    s = 0
    # MORE chaos - use way more objects
    for _ in range(500):  # 10x more chaos
        s ^= id(object())
    
    # Add multiple LCG passes with DIFFERENT constants
    x1 = 1
    x2 = 1
    x3 = 1
    for i in range(10000):  # 2x longer
        x1 = (x1 * 1664525 + 1013904223) & 0xFFFFFFFF
        x2 = (x2 * 22695477 + 1) & 0xFFFFFFFF  # Different LCG
        x3 = (x3 * 48271) & 0x7FFFFFFF  # Another different LCG
        
        s ^= x1 << (i % 8)
        s ^= x2 >> (i % 11)
        s ^= x3 << (i % 13)
        
        # More bit mixing
        s ^= (s << 13) & 0xFFFFFFFF
        s ^= (s >> 7)
        s ^= (s << 17) & 0xFFFFFFFF
        s ^= (s >> 5)
        s ^= (s << 11) & 0xFFFFFFFF
    
    return s & 0x7FFFFFFF

seed = build_seed()
print("Seed:", seed)

# -------- MULTIPLE RNGs FOR MAXIMUM CHAOS --------
def rand1():
    global seed
    seed = (1103515245 * seed + 12345) & 0x7FFFFFFF
    seed ^= id(seed)
    seed ^= (seed << 15) & 0xFFFFFFFF
    seed ^= (seed >> 12)
    return seed / 0x7FFFFFFF

def rand2():
    global seed
    seed = (22695477 * seed + 1) & 0x7FFFFFFF
    seed ^= id(object())  # MORE ID CHAOS
    seed ^= (seed >> 9)
    seed ^= (seed << 21) & 0xFFFFFFFF
    return seed / 0x7FFFFFFF

def rand3():
    global seed
    seed = (48271 * seed) & 0x7FFFFFFF
    seed ^= id([])  # EVEN MORE ID CHAOS
    seed ^= (seed << 7)
    seed ^= (seed >> 14)
    return seed / 0x7FFFFFFF

def rand_range(a, b):
    # Use ALL THREE RNGs and mix them
    r = (rand1() + rand2() + rand3()) / 3.0
    return a + (b - a) * r

# -------- BIGGER GRIDS = MORE CHAOS --------
def make_grid():
    return [[rand_range(-1, 1) for _ in range(32)] for _ in range(32)]  # 32x32 now!

# -------- Matrix multiply -------- 
def matmul(A, B):
    n = len(A)
    R = [[0.0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            s = 0.0
            for k in range(n):
                s += A[i][k] * B[k][j]
            R[i][j] = s
    return R

# -------- Matrix ADD (element-wise) --------
def matadd(A, B):
    n = len(A)
    R = [[0.0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            R[i][j] = A[i][j] + B[i][j]
    return R

# -------- Matrix HADAMARD product (element-wise multiply) --------
def mathadamard(A, B):
    n = len(A)
    R = [[0.0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            R[i][j] = A[i][j] * B[i][j]
    return R

# -------- Build FIVE grids --------
print("\nGenerating grids...")
A = make_grid()
B = make_grid()
C = make_grid()
E = make_grid()
F = make_grid()

# -------- THE CHAOS MIXING --------
print("Mixing grids with pure chaos...")

# Step 1: A * B
D1 = matmul(A, B)
print("  A × B done")

# Step 2: C * E
D2 = matmul(C, E)
print("  C × E done")

# Step 3: Add them
D3 = matadd(D1, D2)
print("  (A×B) + (C×E) done")

# Step 4: Hadamard with F (element-wise multiply)
D4 = mathadamard(D3, F)
print("  ((A×B) + (C×E)) ⊙ F done")

# Step 5: Multiply result by itself (SQUARE IT)
D5 = matmul(D4, D4)
print("  Final² done")

# Step 6: Add original grids back in for MORE CHAOS
D = D5
for i in range(32):
    for j in range(32):
        D[i][j] += A[i][j] * 0.1
        D[i][j] += B[i][j] * 0.2
        D[i][j] += C[i][j] * 0.15

# -------- Flatten and shift --------
values = [v for row in D for v in row]
gmin, gmax = min(values), max(values)
values = [v - gmin for v in values]
gmin, gmax = 0, gmax - gmin

print(f"\nFinal chaos grid: {len(values)} values")
print(f"Range: [{gmin:.3f}, {gmax:.3f}]")

# -------- CHAOTIC PASSWORD GENERATION --------
charset = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()-_=+[]{}|;:,.<>?/~`"
clen = len(charset)

password = ""
used = set()

print("\nGenerating password with MAXIMUM CHAOS...")

# Make password LONGER
for iteration in range(24):  # 24 character password
    # Pick a random target using ALL THREE RNGs
    target = rand_range(gmin, gmax)
    
    # Add MORE randomness to selection
    target += rand1() * (gmax - gmin) * 0.01
    target += rand2() * (gmax - gmin) * 0.01
    target += rand3() * (gmax - gmin) * 0.01
    target = max(gmin, min(gmax, target))  # Keep in bounds
    
    best_i = None
    best_d = 1e9
    
    for i, v in enumerate(values):
        if i in used:
            continue
        d = abs(v - target)
        if d < best_d:
            best_d = d
            best_i = i
    
    if best_i is None:
        # If we run out, just pick randomly from unused
        unused = [i for i in range(len(values)) if i not in used]
        if unused:
            idx = int(rand1() * len(unused))
            idx = min(idx, len(unused) - 1)  # Safety clamp
            best_i = unused[idx]
        else:
            raise RuntimeError("No available value to pick!")
    
    used.add(best_i)
    chosen_val = values[best_i]
    
    # MORE CHAOS in the conversion
    num = chosen_val * 1_000_000
    num += int(rand1() * 1000)  # Add random noise
    num = int(num * rand2())  # Multiply by random
    num ^= int(rand3() * 0xFFFFFF)  # XOR with random
    
    char_index = int(num) % clen
    password += charset[char_index]

print("\n" + "="*50)
print("FINAL CHAOTIC PASSWORD:", password)
print("="*50)
print(f"\nPassword length: {len(password)}")
print(f"Charset size: {clen}")
print(f"Possible combinations: {clen}^{len(password)} ≈ {clen**len(password):.2e}")

# Save to database
save_password(password_use, password)