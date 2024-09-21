import subprocess
import sys
import importlib
import os

def check_python_version():
    return sys.version_info >= (3, 7)

def check_package_installed(package):
    try:
        importlib.import_module(package)
        return True
    except ImportError:
        return False

def check_file_exists(filename):
    return os.path.exists(filename)

def check_docstrings(filename):
    with open(filename, 'r') as f:
        content = f.read()
    return '"""' in content

def check_git_history():
    result = subprocess.run(['git', 'log', '--oneline'], capture_output=True, text=True)
    return len(result.stdout.splitlines()) > 0

def check_code_implementation(filename):
    with open(filename, 'r') as f:
        content = f.read()
    required_functions = ['format_code', 'analyze_code', 'connect_ssh', 'micropico_operation']
    return all(func in content for func in required_functions)

def main():
    checks = {
        "Python 3.7+": check_python_version(),
        "Black installed": check_package_installed("black"),
        "MicroPico installed": check_package_installed("micropico"),
        "Paramiko installed": check_package_installed("paramiko"),
        "student_project.py exists": check_file_exists("student_project.py"),
        "README.md exists": check_file_exists("README.md"),
        ".gitignore exists": check_file_exists(".gitignore"),
        "Docstrings added": check_docstrings("student_project.py"),
        "Git history exists": check_git_history(),
        "Required functions implemented": check_code_implementation("student_project.py")
    }

    all_passed = True
    for check, result in checks.items():
        status = 'Passed' if result else 'Failed'
        print(f"{check}: {status}")
        if not result:
            all_passed = False
            if check == "Python 3.7+":
                print("  Hint: Make sure you're using Python 3.7 or higher.")
            elif "installed" in check:
                print(f"  Hint: Try running 'pip install {check.split()[0].lower()}'")
            elif "exists" in check:
                print(f"  Hint: Create the {check.split()[0]} file in your project directory.")
            elif check == "Docstrings added":
                print("  Hint: Use the autoDocstring extension to add docstrings to all functions.")
            elif check == "Git history exists":
                print("  Hint: Make sure you've made at least one commit to your repository.")
            elif check == "Required functions implemented":
                print("  Hint: Ensure all required functions are present in student_project.py")

    if all_passed:
        print("\nCongratulations! All checks passed. Your submission is ready.")
        print("You can now commit your changes and push to your Git repository.")
    else:
        print("\nSome checks failed. Please address the issues and run this script again.")

if __name__ == "__main__":
    main()
