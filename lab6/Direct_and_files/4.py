def count_lines(file_path):
    with open(file_path, 'r',encoding = 'utf-8') as file:
        line_count = sum(1 for line in file)
    print("Number of lines:", line_count)

file_path = '\\Users\\Айжан\\Desktop\\ПП2\\lab6\\direct_and_files\\row.txt'
count_lines(file_path)
