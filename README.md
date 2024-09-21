# VS Code Development Environment Setup Assignment

## Introduction

This assignment is designed to familiarize you with setting up a VS Code development environment, including installing necessary extensions, managing Python environments with Miniconda, and practicing some basic development tools and techniques.

## Task Checklist

1. Environment Setup
   - Install VS Code
   - Install Miniconda
   - Create a new Conda environment: `conda create -n vscode_setup python=3.9`

2. VS Code Configuration
   Install the following VS Code extensions:
   - Python
   - Pylance
   - Black Formatter
   - MicroPico
   - GitHub Copilot Chat
   - autoDocstring

3. Project Initialization
   - Create a new project folder
   - Open the folder in VS Code
   - Create a `student_project.py` file and copy the provided template code

4. Dependency Installation
   Run: `pip install black micropico paramiko`

5. Code Implementation
   - Complete all TODO tasks in `student_project.py`
   - Use the autoDocstring extension to add docstrings to all functions
   - Use Black to format your code

6. Documentation
   Create a README.md file with project description, installation instructions, and usage guidelines

7. Version Control
   - Initialize a Git repository: `git init`
   - Create a .gitignore file with appropriate Python project ignore rules
   - Add and commit your changes:
     ```
     git add .
     git commit -m "Initial commit"
     ```

## How to Complete the Assignment

1. Follow the task checklist step by step to complete each task.
2. After completing all tasks, run the provided `check_submission.py` script to validate your work:
   ```
   python check_submission.py
   ```
3. If all checks pass, you will see a success message. If any checks fail, please fix the issues based on the provided hints.
4. Once all checks pass, push your final code to your GitHub repository.

## Notes

- Ensure your code runs on Python 3.7 or higher.
- Read each TODO comment carefully to understand and correctly implement all requirements.
- If you encounter any issues while completing the assignment, don't hesitate to ask your instructor for help.

Good luck with your assignment!
