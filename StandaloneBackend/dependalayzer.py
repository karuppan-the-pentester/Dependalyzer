import os
import subprocess
from urllib.parse import urlparse
import sys

def install_dependency(package):
    subprocess.run(['pip', 'install', package])
    subprocess.run(['pip', 'freeze', '>', 'requirements.txt'], shell=True)

def run_project(git_url):
    # Parse the Git URL to extract the repository name
    parsed_url = urlparse(git_url)
    repo_name = os.path.splitext(os.path.basename(parsed_url.path))[0]
    
    # Move into the cloned repository directory
    os.chdir(repo_name)

    # Check if there's a main file to run (adjust as needed)
    main_files = ['Vanakkam_NanbaFW.py', 'app.py']
    for main_file in main_files:
        if os.path.isfile(main_file):
            try:
                # Run the project
                subprocess.run(['python3', main_file])
            except ModuleNotFoundError as e:
                # Extract the missing module name from the error message
                missing_module = str(e).split("'")[1]
                print(f"Installing missing dependency: {missing_module}")
                
                # Install the missing module
                install_dependency(missing_module)
                
                # Retry running the project
                subprocess.run(['python3', main_file])
            break
    else:
        print(f"No main file found in {repo_name}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <git_url>")
        sys.exit(1)

    git_url = sys.argv[1]  
    run_project(git_url)
