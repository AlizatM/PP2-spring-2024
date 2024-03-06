import os

def list_directories_files(path):
    print("Directories:")
    for dir_entry in os.listdir(path):
        if os.path.isdir(os.path.join(path, dir_entry)):
            print(dir_entry)
    print("\nFiles:")
    for file_entry in os.listdir(path):
        if os.path.isfile(os.path.join(path, file_entry)):
            print(file_entry)

def list_all_directories_files(path):
    for root, dirs, files in os.walk(path):
        print("Directory:", root)
        print("Directories:")
        for dir_name in dirs:
            print(os.path.join(root, dir_name))
        print("Files:")
        for file_name in files:
            print(os.path.join(root, file_name))
        print()

path = '\\Users\\Айжан\\Desktop\\ПП2\\lab1'
list_directories_files(path)
print("\nAll directories and files:")
list_all_directories_files(path)
