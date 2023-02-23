if __name__ == '__main__':
    f_name = 'dz19_01.txt'
    f_text = ['Замена строки в текстовом файле;', 'изменить строку в списке;', 'записать список в файл;']

    with open(f_name, 'w') as my_file:  # Запись начального файла
        my_file.write('\n'.join(f_text))

    with open(f_name, 'r+') as my_file: # Чтение с перестановкой
        r_text = ''.join(my_file.readlines()).split('\n') # Если так не перебрать, то лишние \n возникают в файле
        print(f'\033[3m\033[34mИсходный файл:\033[0m\n{(chr(10) + chr(13)).join(r_text)}\033[32m')
        pos1 = int(input('pos1 = ') or 1)
        pos2 = int(input('pos2 = ') or 2)
        r_text[pos1], r_text[pos2] = r_text[pos2], r_text[pos1]
        my_file.seek(0)
        my_file.write('\n'.join(r_text))

    with open(f_name, 'r') as my_file: # Проверочное чтение
        r_text = my_file.readlines()
        print(f'\033[3m\033[34mИзмененный файл:\033[0m\n{"".join(r_text)}\033[0m')