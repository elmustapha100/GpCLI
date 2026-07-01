# GPA Calculator CLI

A simple Python command-line GPA and CGPA calculator designed for Nigerian university grading.

## What it does

- Collects course details per semester: course code, credit units, and grade
- Calculates semester GPA using the weighted formula:
  - `GPA = Σ(units × grade point) ÷ Σ(units)`
- Computes session CGPA when two semesters are available
- Supports a 5.0 grading system out of the box

## Project structure

- `main.py` — the CLI entry point and user flow
- `calculator.py` — GPA/CGPA calculation logic
- `grading.py` — grade-to-point conversion rules
- `category.py` — class-of-degree classification helper

## Usage

1. Run the program:
   - `python3 main.py`
2. Enter the number of courses for the semester
3. For each course, enter:
   - course code
   - course unit
   - grade
4. View the semester GPA
5. Optionally enter semester 2 to compute session CGPA

.

