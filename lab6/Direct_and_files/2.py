import os

def check_access(path):
    exists = os.path.exists(path)
    readable = os.access(path, os.R_OK)
    writable = os.access(path, os.W_OK)
    executable = os.access(path, os.X_OK)
    
    print("Path exists:", exists)
    print("Readable:", readable)
    print("Writable:", writable)
    print("Executable:", executable)

path = '\\Users\\Айжан\\Desktop\\ПП2\\lab1'
check_access(path)
