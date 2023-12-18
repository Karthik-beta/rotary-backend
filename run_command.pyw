import subprocess
import os

def run_server():
    # Set the path to the directory
    directory_path = r"D:\Getin_Solution\rotary-backend\backend"

    try:
        # Change the current working directory to the specified path
        os.chdir(directory_path)

        # Run the command using subprocess
        command = "python manage.py runserver 0.0.0.0:8000"
        subprocess.run(command, shell=True)

    except FileNotFoundError:
        print(f"Directory not found: {directory_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_server()
