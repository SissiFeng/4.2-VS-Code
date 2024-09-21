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

def check_vscode_extension(extension):
    result = subprocess.run(['code', '--list-extensions'], capture_output=True, text=True)
    return extension.lower() in result.stdout.lower()

def check_file_exists(filename):
    return os.path.exists(filename)

def check_git_repo():
    return os.path.exists('.git')

def check_docstrings(filename):
    with open(filename, 'r') as f:
        content = f.read()
    return '"""' in content

def main():
    checks = {
        "Python 3.7+": check_python_version(),
        "Black installed": check_package_installed("black"),
        "Pylance extension": check_vscode_extension("ms-python.vscode-pylance"),
        "MicroPico installed": check_package_installed("micropico"),
        "GitHub Copilot Chat extension": check_vscode_extension("github.copilot-chat"),
        "SSH package (paramiko) installed": check_package_installed("paramiko"),
        "autoDocstring extension": check_vscode_extension("njpwerner.autodocstring"),
        "Student project file exists": check_file_exists("student_project.py"),
        "README.md exists": check_file_exists("README.md"),
        "Git repository initialized": check_git_repo(),
        ".gitignore exists": check_file_exists(".gitignore"),
        "Docstrings added": check_docstrings("student_project.py")
    }

    all_passed = True
    for check, result in checks.items():
        print(f"{check}: {'Passed' if result else 'Failed'}")
        if not result:
            all_passed = False

    if all_passed:
        print("\nAll checks passed! Your environment is set up correctly and all tasks are completed.")
    else:
        print("\nSome checks failed. Please review your setup and tasks, then try again.")

if __name__ == "__main__":
    main()
