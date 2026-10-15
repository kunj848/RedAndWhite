# Red & White Multimedia - Python Projects

This repository contains Python projects and practical implementations developed for Red & White Skill Education coursework.

---

## 📌 Projects Directory

1. **[Project 1: Interactive Personal Data Collector GUI (`project1.py`)](#-project-1-interactive-personal-data-collector-gui)**
2. **[Project 2: Logic Box (`logic_box.py`)](#-project-2-logic-box---pattern-generator--number-analyzer)**
3. **[Project 3: Student Data Organizer (`master_program3.py`)](#-project-3-student-data-organizer)**

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

## 📚 Project 3: Student Data Organizer

`master_program3.py` is a robust, menu-driven console application designed for student record management (CRUD operations). It demonstrates core Python programming concepts including:
- **Dictionary Data Structures**: Fast key-value retrieval, nested records, and in-memory data management.
- **Set Comprehension & Uniqueness**: Extracting and sorting unique subjects across all students.
- **Input Validation & Exception Handling**: Utilizing `datetime.strptime()` for date formatting and `try-except` blocks for numeric validations.
- **Safe Partial Updates**: Retaining previous values when fields are left blank on Enter.
- **Action Confirmation**: Deletion confirmations to prevent accidental data loss.

---

### 💻 How to Run

```bash
python master_program3.py
```

---

### 📋 Complete Program Output & Interaction Walkthrough

#### 1. Main Menu
```text
========================================
 Welcome to Student Data Organizer 
========================================
1. Add Student
2. Display All Students
3. Update Student Information
4. Delete Student
5. Display Subjects Offered
6. Exit
Enter your choice (1-6): 1
```

#### 2. Adding Students (`Add Student`)
```text
--- Add Student ---
Student ID: 101
Name: Alice Johnson
Age: 20
Grade: A
Date of Birth (YYYY-MM-DD): 2004-05-15
Subjects (comma-separated): Mathematics, Physics, Computer Science
Student added successfully!

========================================
 Welcome to Student Data Organizer 
========================================
1. Add Student
2. Display All Students
3. Update Student Information
4. Delete Student
5. Display Subjects Offered
6. Exit
Enter your choice (1-6): 1

--- Add Student ---
Student ID: 102
Name: Bob Smith
Age: 22
Grade: B
Date of Birth (YYYY-MM-DD): 2002-11-20
Subjects (comma-separated): English, Chemistry, Physics
Student added successfully!
```

#### 3. Displaying All Students (`Display All Students`)
```text
Enter your choice (1-6): 2

--- All Students ---
----------------------------------------
Student ID : 101
Name       : Alice Johnson
Age        : 20
Grade      : A
Date of Birth: 2004-05-15
Subjects   : Mathematics, Physics, Computer Science
----------------------------------------
Student ID : 102
Name       : Bob Smith
Age        : 22
Grade      : B
Date of Birth: 2002-11-20
Subjects   : English, Chemistry, Physics
```

#### 4. Displaying Unique Subjects Offered (`Display Subjects Offered`)
```text
Enter your choice (1-6): 5

--- Subjects Offered ---
1. Chemistry
2. Computer Science
3. English
4. Mathematics
5. Physics
```

#### 5. Updating a Student Record (`Update Student Information`)
*(Pressing Enter retains the existing value)*
```text
Enter your choice (1-6): 3

Enter Student ID to update: 101
Press Enter to keep the existing value.
Name [Alice Johnson]: Alice J.
Age [20]: 21
Grade [A]: 
DOB [2004-05-15]: 
Subjects [Mathematics, Physics, Computer Science]: Mathematics, Data Science, AI
Student information updated successfully!
```

#### 6. Deleting a Student Record (`Delete Student`)
```text
Enter your choice (1-6): 4

Enter Student ID to delete: 102
Delete Bob Smith? (yes/no): yes
Student deleted successfully!
```

#### 7. Input Validation & Error Handling Examples

- **Duplicate Student ID:**
  ```text
  Enter your choice (1-6): 1

  --- Add Student ---
  Student ID: 101
  Student ID already exists!
  ```

- **Invalid Age:**
  ```text
  --- Add Student ---
  Student ID: 103
  Name: Charlie
  Age: -5
  Age must be greater than 0.
  ```

- **Invalid Date of Birth:**
  ```text
  --- Add Student ---
  Student ID: 103
  Name: Charlie
  Age: 19
  Grade: A
  Date of Birth (YYYY-MM-DD): 25-12-2005
  Invalid date! Use YYYY-MM-DD.
  ```

- **Student Not Found (Update/Delete):**
  ```text
  Enter Student ID to update: 999
  Student not found!
  ```

#### 8. Exit Program
```text
Enter your choice (1-6): 6
Thank you for using Student Data Organizer!
```

---

## 🛠️ Requirements

- **Python 3.8+**
- Standard Python libraries (`math`, `tkinter`, `datetime` — no external pip dependencies required).

---

## 👤 Author
- **GitHub**: [@kunj848](https://github.com/kunj848)
