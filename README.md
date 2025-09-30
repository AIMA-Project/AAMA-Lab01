# AI-Assisted Malware Analysis Lab 01: Feature Extraction and Data Encoding

**Modified and Enhanced by:** Ubayeid U.
**Original Project:** AIMA-Project/AAMA-Lab01

Welcome! This lab teaches you how to extract features from Windows executable files (PE files) and encode them for machine learning analysis. You'll learn to use Python and the LIEF library to analyze malware.

## 📋 Table of Contents

- [What You'll Learn](#what-youll-learn)
- [Prerequisites](#prerequisites)
- [Quick Start Guide](#quick-start-guide)
- [Lab Structure](#lab-structure)
- [Detailed Setup Instructions](#detailed-setup-instructions)
- [Running the Labs](#running-the-labs)
- [Testing Your Work](#testing-your-work)
- [Troubleshooting](#troubleshooting)
- [Project Files Explained](#project-files-explained)

## 🎯 What You'll Learn

- **Feature Extraction**: How to extract meaningful data from Windows executable files
- **Data Encoding**: How to convert extracted features into formats suitable for machine learning
- **Malware Analysis**: Understanding PE file structure and suspicious patterns
- **Python Programming**: Working with libraries, virtual environments, and testing

## 📚 Prerequisites

- **Python 3.7+** installed on your computer
- **Basic command line knowledge** (we'll guide you through everything!)
- **Windows, Mac, or Linux** (instructions for all platforms)

Don't worry if you're new to virtual environments or unit testing - this guide explains everything!

## 🚀 Quick Start Guide

### Step 1: Get the Code

```bash
git clone https://github.com/AIMA-Project/AAMA-Lab01
cd AAMA-Lab01
```

### Step 2: Set Up Python Environment

**Windows:**

```powershell
python -m venv myenv
myenv\Scripts\Activate.ps1
pip install -r requirements.txt
```

**Mac/Linux:**

```bash
python3 -m venv myenv
source myenv/bin/activate
pip install -r requirements.txt
```

### Step 3: Run the Labs

```bash
# Run Lab 1a (basic feature extraction)
python FeatureExtraction1a.py ExamplePE.exe

# Run Lab 1b (feature extraction + encoding)
python FeatureExtraction1b.py ExamplePE.exe
```

### Step 4: Test Your Work

```bash
# Test Lab 1a
python -m unittest GradeScript1a.py

# Test Lab 1b
python -m unittest GradeScript1b.py
```

## 🏗️ Lab Structure

### Lab 1a: Basic Feature Extraction

**Goal**: Extract key features from a Windows executable file

- File hash (SHA-256)
- File size information
- Target architecture (x86, x64, etc.)
- Section information and entropy values

### Lab 1b: Advanced Feature Extraction + Encoding

**Goal**: Extract features AND encode them for machine learning

- Everything from Lab 1a
- One-hot encoding for machine types
- Numerical encoding for section names
- Data preparation for ML algorithms

## 📖 Detailed Setup Instructions

### What is a Virtual Environment?

A virtual environment is like a separate, clean workspace for your Python project. It prevents conflicts between different projects and keeps your system clean.

Think of it like having a separate toolbox for each project - your tools don't get mixed up!

### Setting Up Your Virtual Environment

1. **Create the environment** (like creating a new toolbox):

   ```bash
   python -m venv myenv
   ```

2. **Activate the environment** (like opening your toolbox):

   **Windows:**

   ```powershell
   myenv\Scripts\Activate.ps1
   ```

   **Mac/Linux:**

   ```bash
   source myenv/bin/activate
   ```

   You'll see `(myenv)` at the start of your command prompt when it's active.

3. **Install required packages** (like putting tools in your toolbox):
   ```bash
   pip install -r requirements.txt
   ```

### What Gets Installed?

- **LIEF**: A library for analyzing executable files
- **Standard Python libraries**: For file operations, hashing, etc.

## 🧪 Running the Labs

### Understanding the Output

When you run the scripts, you'll see output like:

```
1df56772594a5ec2f550c7727a4879142736106da68b5d185c4391e08b48ec5e  # SHA-256 hash
446464                                                              # Header size
446464                                                              # Virtual size
I386                                                                # Architecture
5                                                                   # Number of sections
{'.text': 6.4723, '.rdata': 5.2098, '.data': 4.1106, '.ndata': 0.0, '.rsrc': 5.732}  # Section entropy
```

**What This Means:**

- **Hash**: Unique fingerprint of the file
- **Sizes**: How big the file is in memory
- **Architecture**: What type of processor it's built for
- **Sections**: Different parts of the executable (code, data, resources)
- **Entropy**: Measure of randomness (high entropy might indicate encryption/packing)

## 🧪 Testing Your Work

### What are Unit Tests?

Unit tests automatically check if your code works correctly. Think of them like automated grading - they run your code and verify the output matches what's expected.

### Running Tests

```bash
# Test basic feature extraction
python -m unittest GradeScript1a.py

# Test advanced feature extraction + encoding
python -m unittest GradeScript1b.py
```

### Understanding Test Results

- **`.` (dot)**: Test passed ✅
- **`F`**: Test failed ❌
- **`E`**: Test had an error 💥

Example successful output:

```
......
----------------------------------------------------------------------
Ran 6 tests in 0.123s

OK
```

## 🔧 Troubleshooting

### Common Issues

**"No module named 'lief'"**

- **Solution**: Make sure your virtual environment is activated and run `pip install -r requirements.txt`

**"Cannot find file 'ExamplePE.exe'"**

- **Solution**: Make sure you're running the command from the main lab directory

**Virtual environment not activating**

- **Windows**: Try `myenv\Scripts\activate.bat` instead of `.ps1`
- **Mac/Linux**: Make sure you're using `source` before the activate command

**Permission errors on Windows**

- **Solution**: Try running PowerShell as Administrator, or use `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`

### Getting Help

If you're stuck:

1. Check that your virtual environment is active (you see `(myenv)` in your prompt)
2. Verify you're in the correct directory
3. Make sure all files are present
4. Try deactivating and reactivating your virtual environment

## 📁 Project Files Explained

```
AAMA-Lab01/
├── README.md                    # This file - your guide!
├── requirements.txt             # List of Python packages needed
├── ExamplePE.exe               # Sample Windows executable for analysis
├── FeatureExtraction1a.py      # Lab 1a: Basic feature extraction
├── FeatureExtraction1b.py      # Lab 1b: Advanced extraction + encoding
├── GradeScript1a.py           # Tests for Lab 1a
├── GradeScript1b.py           # Tests for Lab 1b
├── myenv/                     # Your virtual environment (created by you)
├── deliverables/              # Where you put completed work
└── .github/                   # GitHub configuration (ignore this)
```

### Key Files You'll Work With:

- **FeatureExtraction1a.py**: Your main Lab 1a script
- **FeatureExtraction1b.py**: Your main Lab 1b script
- **ExamplePE.exe**: The file you'll analyze (Notepad++ installer)
- **GradeScript\*.py**: Automated tests to check your work

## 🎓 Learning Goals

By completing this lab, you'll understand:

- How malware analysts extract features from suspicious files
- Why file entropy matters in malware detection
- How to prepare data for machine learning algorithms
- Python virtual environments and testing
- The structure of Windows executable files

## 🏆 Success Criteria

You've successfully completed the lab when:

- [ ] Both Python scripts run without errors
- [ ] All unit tests pass
- [ ] You understand what each extracted feature means
- [ ] You can explain the difference between raw and encoded features

---

**📧 Need Help?** Ask your instructor or TA if you get stuck!

**�‍💻 Project Enhanced by:** Md Ubayeid Ullah  
**�🔬 Funded by:** National Science Foundation (NSF) Grant #2025682
