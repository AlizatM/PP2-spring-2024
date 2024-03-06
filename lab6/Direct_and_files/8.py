import os

def delete_file(path):
    if os.path.exists(path):
        os.remove(path)
    else:
        print("File does not exist.")

file_path = '\\Users\\Айжан\\Desktop\\ПП2\\lab6\\direct_and_files\\file2.txt'
delete_file(file_path)
