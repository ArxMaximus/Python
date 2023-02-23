if __name__ == '__main__':
    f_in1_name = 'dz19_01.txt'
    f_in2_name = 'dz19_02.txt'
    f_out_name = 'dz19_03.txt'

    # Объединяем и записываем
    with open(f_in1_name, 'r') as f_in1, open(f_in2_name, 'r') as f_in2, open(f_out_name, 'w') as f_out:
        my_text1 = ''.join(f_in1.readlines()).split('\n')
        my_text2 = ''.join(f_in2.readlines()).split('\n')
        f_out.writelines('\n'.join(my_text1 + my_text2))

    # Проверочное чтение
    with open(f_out_name, 'r') as my_file:
        print(''.join(my_file.readlines()))
