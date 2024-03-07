import os
c = 'A'
while c <= 'Z':
    path = r"C:\Users\Нурбек\Desktop\PP2\TSIS6\files\A-Z" + r'\\' + c + ".txt"
    f = open(path, "w")
    f.close()
    c = chr(ord(c) + 1)