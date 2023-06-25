import os
import zipfile
import tempfile
import subprocess

def save_and_open_last_file(zip_path, output_folder, depth=0):
    # The depth argument is used for indentation, to show the nesting levels
    last_file_path = None
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        for filename in zip_ref.namelist():
            if filename.endswith('.zip'):
                # If the file is a zip file, extract it to a temporary directory and then
                # recursively call save_and_open_last_file() on the extracted zip file
                with tempfile.TemporaryDirectory() as tempdir:
                    inner_zip_path = zip_ref.extract(filename, path=tempdir)
                    last_file_path = save_and_open_last_file(inner_zip_path, output_folder, depth + 1)
            else:
                # Save data from current last file
                last_file_path = os.path.join(output_folder, filename)
                with zip_ref.open(filename) as zf, open(last_file_path, 'wb') as f:
                    f.write(zf.read())
    return last_file_path

outer_zip_path = r"C:\Users\monic\Downloads\99problems.zip"
output_folder = r"C:\Users\monic\Downloads"
last_file_path = save_and_open_last_file(outer_zip_path, output_folder)

# Open the file in Notepad (replace 'notepad' with the path of your preferred text editor if not using Notepad)
subprocess.run(['notepad', last_file_path])
