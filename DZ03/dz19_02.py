if __name__ == '__main__':
    f_name = 'dz19_02.txt'
    f_text = ['Замена строки в текстовом файле;', 'изменить строку в списке;', 'записать список в файл']

    with open(f_name, 'w') as my_file:
        my_file.write('\n'.join(f_text))

    with open(f_name, 'r+') as my_file:
        new_text = ''.join(my_file.readlines()).split('\n')
        print(f'\033[3m\033[34mИсходный файл:\033[0m\n{(chr(10) + chr(13)).join(new_text)}\033[0m')
        my_file.seek(0)
        my_file.write('\n'.join(new_text[::-1]))

    with open(f_name, 'r') as my_file:
        new_text = my_file.readlines()
        print(f'\033[3m\033[34mИзмененный файл:\033[0m\n{"".join(new_text)}\033[0m')