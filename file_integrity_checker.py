import hashlib
import os
import json
from datetime import datetime
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext

# ----------- Config ----------- #
HASH_FILE = "hashes.json"
LOG_FILE = "integrity_log.txt"
IGNORE_DIRS = ['venv', '.git']
IGNORE_EXT = ['.pyc', '.log']

# ----------- Core Logic ----------- #

def calculate_hash(file_path):
    sha256 = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            for block in iter(lambda: f.read(4096), b""):
                sha256.update(block)
        return sha256.hexdigest()
    except Exception:
        return None

def scan_directory(directory):
    file_hashes = {}
    for root, dirs, files in os.walk(directory):
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]

        for file in files:
            if file in [HASH_FILE, LOG_FILE]:
                continue
            if any(file.endswith(ext) for ext in IGNORE_EXT):
                continue

            path = os.path.join(root, file)
            file_hash = calculate_hash(path)
            if file_hash:
                file_hashes[path] = file_hash
    return file_hashes

def load_old_hashes():
    if os.path.exists(HASH_FILE):
        try:
            with open(HASH_FILE, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return {}
    return {}

def save_hashes(hashes):
    with open(HASH_FILE, "w") as f:
        json.dump(hashes, f, indent=4)

def log_change(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a") as f:
        f.write(f"[{timestamp}] {message}\n")

def compare_hashes(old, new):
    results = []

    for file in new:
        if file not in old:
            msg = f"[NEW FILE] {file}"
            results.append(msg)
            log_change(msg)
        elif old[file] != new[file]:
            msg = f"[MODIFIED] {file}"
            results.append(msg)
            log_change(msg)

    for file in old:
        if file not in new:
            msg = f"[DELETED] {file}"
            results.append(msg)
            log_change(msg)

    return results

# ----------- GUI ----------- #

def select_directory():
    folder = filedialog.askdirectory()
    if folder:
        entry_path.delete(0, tk.END)
        entry_path.insert(0, folder)

def run_check():
    directory = entry_path.get().strip()
    if not os.path.exists(directory):
        messagebox.showerror("Error", "Selected directory does not exist.")
        return

    output_box.delete(1.0, tk.END)

    old_hashes = load_old_hashes()
    new_hashes = scan_directory(directory)
    changes = compare_hashes(old_hashes, new_hashes)
    save_hashes(new_hashes)

    if changes:
        for change in changes:
            output_box.insert(tk.END, change + "\n")
    else:
        output_box.insert(tk.END, "No changes detected.\n")

    output_box.insert(tk.END, "\nFile integrity check completed.\n")

# ----------- Main Window ----------- #

app = tk.Tk()
app.title("File Integrity Checker")
app.geometry("700x400")

tk.Label(app, text="Select Directory to Monitor:", font=("Arial", 11)).pack(pady=5)

entry_path = tk.Entry(app, width=80)
entry_path.pack(pady=5)

tk.Button(app, text="Browse", command=select_directory).pack(pady=5)
tk.Button(app, text="Run Integrity Check", command=run_check).pack(pady=5)

output_box = scrolledtext.ScrolledText(app, width=85, height=15)
output_box.pack(pady=10)

app.mainloop()
