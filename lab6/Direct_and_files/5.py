def write_list_to_file(file_path, data):
    with open(file_path, 'w') as file:
        for item in data:
            file.write(str(item) + ' ')

file_path = '\\Users\\Айжан\\Desktop\\ПП2\\lab6\\direct_and_files\\row.txt'
data = ['1', '2', '3']
write_list_to_file(file_path, data)
