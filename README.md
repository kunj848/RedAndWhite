# Red & White Multimedia - Python Projects

This repository contains Python projects and practical implementations developed for Red & White Skill Education coursework.

---

## 📌 Projects Directory

1. **[Project 1: Interactive Personal Data Collector GUI (`project1.py`)](#-project-1-interactive-personal-data-collector-gui)**
2. **[Project 2: Logic Box (`logic_box.py`)](#-project-2-logic-box---pattern-generator--number-analyzer)**

---

## 🚀 Project 2: Logic Box - Pattern Generator & Number Analyzer

`logic_box.py` is a menu-driven Python application designed to practice fundamental programming concepts:
- **Control Structures & Conditionals** (`if-elif-else`)
- **Loops** (`for` and `while`)
- **The `range()` function**
- **Control Statements** (`break`, `continue`, `pass`)
- **Nested Loops** for pattern generation
- **Robust Input Validation & Error Handling**

### ✨ Key Features

1. **Pattern Generator**:
   - Prompts the user dynamically for the number of rows.
   - Generates a classic right-angled triangle pattern of `*` using nested loops.
   - Validates that the input is a positive integer.
   
2. **Number Analyzer**:
   - Prompts for start and end range boundaries.
   - Iterates using `range(start, end + 1)`.
   - Checks and classifies each number as **Odd** or **Even**.
   - Calculates and displays the total sum of all numbers within the range.
   - Validates range boundaries (`end >= start`).

3. **Menu-Driven Interface**:
   - Continuous `while` loop that keeps the application interactive until the user explicitly selects **Exit (3)**.
   - Clean and descriptive console prompts and exit messaging.

---

### 💻 How to Run

Make sure you have Python 3.x installed on your system.

```bash
python logic_box.py
```

---

### 📋 Example Console Interaction

```text
Welcome to the Pattern Generator and Number Analyzer!

Select an option:
1. Generate a Pattern
2. Analyze a Range of Numbers
3. Exit
Enter your choice: 1
Enter the number of rows for the pattern: 5

Pattern:
*
**
***
****
*****

Select an option:
1. Generate a Pattern
2. Analyze a Range of Numbers
3. Exit
Enter your choice: 2
Enter the start of the range: 10
Enter the end of the range: 15
Number 10 is Even
Number 11 is Odd
Number 12 is Even
Number 13 is Odd
Number 14 is Even
Number 15 is Odd
Sum of all numbers from 10 to 15 is: 75

Select an option:
1. Generate a Pattern
2. Analyze a Range of Numbers
3. Exit
Enter your choice: 3
Exiting the program. Goodbye!
```

---

## 🎨 Project 1: Interactive Personal Data Collector GUI

`project1.py` is a Tkinter-based interactive GUI application featuring:
- Animated modern dark-mode interface (`#0f172a`).
- Real-time profile preview card.
- Animated progress bar and field validations.
- Form controls for personal data collection and formatted summary exports.

### How to Run:
```bash
python project1.py
```

---

## 🛠️ Requirements

- **Python 3.8+**
- Standard Python libraries (`math`, `tkinter`, `datetime` — no external pip dependencies required).

---

## 👤 Author
- **GitHub**: [@kunj848](https://github.com/kunj848)
