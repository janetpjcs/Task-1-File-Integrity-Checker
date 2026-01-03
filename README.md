# 🔐 File Integrity Checker (Python)

A **File Integrity Checker** built using **Python and Tkinter GUI**.  
This tool monitors a selected directory and detects **new, modified, or deleted files** using **SHA-256 cryptographic hashing**.

This project is created as part of a **Cybersecurity / Ethical Hacking Internship task**.

---

## 📌 Features

- GUI-based folder selection
- SHA-256 hashing for file integrity
- Detects:
  - ✅ New files
  - ✏️ Modified files
  - ❌ Deleted files
- Stores hashes securely in JSON format
- Maintains a log file with timestamps
- Automatically ignores:
  - `venv/`
  - `.git/`
  - `.pyc` and `.log` files

---

## 🛠️ Technologies Used

- Python 3
- Tkinter (GUI)
- hashlib (Cryptographic hashing)
- JSON
- OS module


> ⚠️ **Note:** The virtual environment folder (`venv/`) is intentionally **NOT uploaded** to GitHub.

---

## ⚙️ How It Works (Simple Explanation)

1. User selects a folder using the GUI.
2. The program scans all files in the selected directory.
3. A **SHA-256 hash** is generated for each file.
4. Hash values are stored in `hashes.json`.
5. When the program is run again:
   - New files are detected
   - Modified files are detected
   - Deleted files are detected
6. All changes are:
   - Displayed in the GUI
   - Logged in `integrity_log.txt` with timestamps

---

# Task-1: File Integrity Checker

## Project Structure

```
codtech-cybersecurity-ethicalhacking-internship/
└── Task-1_File-Integrity-Checker/
    ├── file_integrity_checker.py
    ├── hashes.json
    ├── integrity_log.txt
    ├── README.md
    ├── testfiles/
    │   ├── file1.txt
    │   ├── file2.txt
    │   ├── file3.txt
    │   └── file4.txt
    └── screenshots/
        └── output.png
```

## ▶️ How to Run the Project

### 1️⃣  Create Virtual Environment
### 2️⃣ Run the Program
        python file_integrity_checker.py
### 3️⃣ Use the GUI
        Click Browse
        Select a folder to monitor
        Click Run Integrity Check
        View results in the output window    
###  🖼️ Screenshots

Screenshots showing the program execution and output are stored in the screenshots/ folder.    
