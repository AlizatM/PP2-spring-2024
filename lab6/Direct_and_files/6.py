import string
import os

def generate_text_files(directory):
    for letter in string.ascii_uppercase:
        file_name = os.path.join(directory, letter + '.txt')
        with open(file_name, 'w') as file:
            file.write("This is file " + file_name)

directory = '\\Users\\Айжан\\Desktop\\ПП2\\lab6\\direct_and_files\\file'
generate_text_files(directory)
