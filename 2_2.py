import os
import re
path = r"C:\Users\Нурбек\Desktop\PP2\TSIS6\files\2_1.py"

if os.access(path, os.F_OK):
    print("exists")
if os.access(path, os.R_OK):
    print("readable")
if os.access(path, os.W_OK):
    print("writeable")
if os.access(path, os.EX_OK):
    print("executable")