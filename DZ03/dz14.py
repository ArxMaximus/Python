s = 'I am learning Python. hello, WORLD!'

print('Задание 1')
print(s[:s.find('h')] + s[s.rfind('h') + 1:])

print('\nЗадание 2')
print(s[:s.find('h') + 1] + s[s.rfind('h') - 1:s.find('h'):-1] + s[s.rfind('h'):])

print('\nЗадание 3')
st = input('Строка:') or '11 23 44 55 23 22'        # Значения по умолчанию, если пустой ввод
sub_st = input('Ее заменяемая подстрока:') or '23'
new_sub = input('Новая подстрока:') or '!!!'

print(st.replace(sub_st, new_sub))

print('\nЗадание 4')
txt = """Ежевику для ежат
Принесли два ежа
Ежевику еле-еле
Ежата возле ели съели."""

print(f'{txt} ({len(list(filter(lambda w: w[0].lower() == "е", txt.split())))} слов)')
