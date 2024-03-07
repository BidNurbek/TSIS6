import os

path = r"C:\Users\Нурбек\Desktop\PP2\TSIS6\files\2.txt"

if os.access(path, os.F_OK) and os.path.exists(path):
    os.remove(path)