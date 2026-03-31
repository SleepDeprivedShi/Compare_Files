# File Integrity Checker – Folder Scan & Compare Tool

A desktop application built with PyQt6 to scan directories, generate file metadata, and compare scans to detect missing, extra, or modified files.

---

## Features

- Recursive folder scanning (includes all subdirectories)
- Two scan modes:
  - Size Mode (fast)
  - MD5 Mode (accurate)
- Export scan results to JSON
- Compare two scans to detect:
  - Missing files
  - Extra files
  - Modified files (size or hash mismatch)
- Real-time progress tracking:
  - Progress bar (percentage)
  - Currently scanning file display
- Responsive UI using threading (QThread)
- Color-coded comparison results

---

## Tech Stack

- Frontend: PyQt6  
- Backend: Python  
- Data Format: JSON  
- Concurrency: QThread  

---

## Project Structure

```text
project/
│
├── main.py        # PyQt6 GUI
├── core.py        # Scanning and comparison logic
└── README.md
```

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/file-integrity-checker.git
cd file-integrity-checker
```

2. Install dependencies:

```bash
pip install PyQt6
```

3. Run the application:

```bash
python main.py
```

---

## Usage

### Scan

1. Open the application  
2. Click "Scan Folder"  
3. Select a directory  
4. Choose scan mode (Size or MD5)  
5. Click "Scan"  
6. Save the generated JSON file  

---

### Compare

1. Click "Compare Scans"  
2. Select two JSON scan files  
3. Click "Compare"  
4. View results in a table:
   - Missing files  
   - Extra files  
   - Mismatched files  

---

## How It Works

### Scanning

- Traverses directories using `os.walk`
- Counts total files before scanning
- Processes each file and updates progress
- Optionally computes MD5 hash

### Progress Tracking

- Real-time percentage updates
- Displays current file being scanned
- Runs in a separate thread using `QThread`

### Comparison

- Loads two JSON scan files
- Compares file paths and metadata
- Detects missing, extra, and mismatched files

---

## Release

Download the executable from the **Releases** section and run directly (no Python required).
