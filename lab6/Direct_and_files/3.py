import os

def path_info(path):
    exists = os.path.exists(path)
    if exists:
        filename = os.path.basename(path)
        directory = os.path.dirname(path)
        print("Path exists.")
        print("Filename:", filename)
        print("Directory:", directory)
    else:
        print("Path does not exist.")

path = '\\Users\\Айжан\\Desktop\\ПП2\\lab1'
path_info(path)
