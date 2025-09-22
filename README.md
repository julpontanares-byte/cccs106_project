# CCCS 106 Projects
Application Development and Emerging Technologies  
Academic Year 2025-2026

## Student Information
- **Name:** Pontanares, Juliet S.
- **Student ID:** 231002289
- **Program:** Bachelor of Science in Computer Science
- **Section:** 3A

## Repository Structure

### Week 1 Labs - Environment Setup and Python Basics
- `week1_labs/hello_world.py` - Basic Python introduction
- `week1_labs/basic_calculator.py` - Simple console calculator

### Week 2 Labs - Git and Flet GUI Development
- `week2_labs/hello_flet.py` - First Flet GUI application
- `week2_labs/personal_info_gui.py` - Enhanced personal information manager
- `week2_labs/enhanced_calculator.py` - GUI calculator (coming soon)

### Week 3 Labs - Flet User Login Application
- `week3_labs/main.py` - User Interface
- `week3_labs/db_connection.py` - Database Connection

### Week 4 Labs - Contact Book Application
- `week4_labs/contact_book_app/src/main.py` - Main Flet UI for contact book
- `week4_labs/contact_book_app/src/database.py` - Contact database initialization and operations
- `week4_labs/contact_book_app/src/app_logic.py` - Logic for displaying and adding contacts
- `week4_labs/contact_book_app/src/contact_db.sqlite` - SQLite database file for storing contacts

### Module 1 Final Project
- `module1_final/` - Final integrated project (TBD)

## Technologies Used
- **Python 3.8+** — Main programming language for all projects
- **Flet 0.28.3** — Cross-platform GUI framework for desktop and web apps
- **Git & GitHub** — Source code management and collaboration
- **VS Code** — Code editor and integrated development environment
- **XAMPP** — Local web server stack for database and backend testing (future use)
- **SQLite** — Lightweight database for storing application data

## Development Environment
- **Virtual Environment:** `cccs106_env` (isolates Python dependencies)
- **Python Packages:** `flet==0.28.3`, `sqlite3` (standard library)
- **Platform:** Windows 10/11
- **Additional Tools:** Git Bash, Command Prompt, and PowerShell for running scripts and managing repositories

## How to Run Applications

### Prerequisites
1. Python 3.8+ installed
2. Virtual environment activated: `cccs106_env\Scripts\activate`
3. Flet installed: `pip install flet==0.28.3`

### Running GUI Applications
```cmd
# Navigate to project directory
cd week1_labs
cd week2_labs
cd week3_labs
cd week4_labs/contact_book_app/src
cd module1_final

# Run applications
python hello_flet.py
python personal_info_gui.py
python contact_book_app.py

# Add the updated README.md file to the staging area
# This stages the modified README.md file so it will be included in the next commit
# Git tracks changes to this file and prepares it for version control
git add README.md

# Commit the staged changes with a descriptive message
# Creates a permanent snapshot of the README.md updates in the repository history
# The commit message should clearly describe what was changed for future reference
git commit -m "Update README.md with new application information"

# Push the committed changes to the remote GitHub repository
# Synchronizes your local main branch with the remote repository on GitHub
# This makes your updated README.md visible to others and backs up your changes
git push origin main
