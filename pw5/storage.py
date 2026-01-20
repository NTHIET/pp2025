import zipfile
import os

files = ["students.txt", "courses.txt", "marks.txt"]
archives = "students.dat"
def compress_files():
    with zipfile.ZipFile(archives, 'w') as z:
        for f in files:
            if os.path.exists(f):
                z.write(f)
                
def decompress_data():
    if not os.path.exists(archives):
        return False
    with zipfile.ZipFile(archives, "r") as z:
        z.extractall()
    return True