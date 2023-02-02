import re

# Задание 1
password = 'my-p@ssw0rd'
reg = '[0-9A-z@_-]{6,18}'
test = re.findall(reg, password)
print(f'Valid password {test}' if test[0] == password else f"Invalid password ['{password}']")

# Задание 2
txt = 'В июне 2021 года, 02/06/2021, 05/06/2021, 14/06/2021, были зафиксированы максимумы ежедневных осадков.'
reg2 = '[0-3]\d/[0-1]\d/[1-2]\d\d\d'
print(re.findall(reg2, txt))
