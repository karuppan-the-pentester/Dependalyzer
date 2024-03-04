import os
import subprocess
import sys
import ast
from urllib.parse import urlparse

def install_dependency(package):
    subprocess.run(['pip', 'install', package])

def scan_repo_for_dependencies(repo_path):
    dependencies = set()

    for root, dirs, files in os.walk(repo_path):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                file_dependencies = scan_file_for_dependencies(file_path)
                dependencies.update(file_dependencies)

    return dependencies

def scan_file_for_dependencies(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        tree = ast.parse(content, filename=file_path)

    dependencies = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                dependencies.add(alias.name)
        elif isinstance(node, ast.ImportFrom):
            dependencies.add(node.module)

    return dependencies

def run_project(git_url):
    # Parse the Git URL to extract the repository name
    parsed_url = urlparse(git_url)
    repo_name = os.path.splitext(os.path.basename(parsed_url.path))[0]

    # Move into the cloned repository directory
    os.chdir(repo_name)

    # Scan the entire repository for dependencies
    dependencies = scan_repo_for_dependencies(os.getcwd())

    # Collect local dependencies (starting with dot '.')
    local_dependencies = {dep for dep in dependencies if dep.startswith('.')}

    # Create requirements.txt file
    with open('requirements.txt', 'w') as req_file:
        for dep in dependencies:
            req_file.write(dep + '\n')

    # Install all dependencies
    for dep in dependencies:
        install_dependency(dep)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py --url=<git_url>")
        sys.exit(1)

    git_url = None

    for arg in sys.argv[1:]:
        if arg.startswith("--url="):
            git_url = arg.split("=")[1]

    if not git_url:
        print("Invalid arguments. Use --url=<git_url>")
        sys.exit(1)

    run_project(git_url)
