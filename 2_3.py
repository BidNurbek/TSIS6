import os


path = r"C:\Users\Нурбек\Desktop\PP2\TSIS6\files\2_1.py"

if os.path.exists(path):
    print("exists")

    print(os.path.split(path))