width = int(input('Введите ширину основания треугольника: '))
method = input('1 - выравнивание по левому краю, 2 - по середине, 3 - по правому: ')

line = '*' * width
while len(line) > 1:
    curLine = line
    if len(curLine) == width:
        curLine = curLine.replace('*', '-')
        if method == '2':
            line = line[:-2]
        else:
            line = line[:-1]
    else:
        match method:
            case '2':
                curLine = ('\\' + curLine[1: -1] + '/').center(width)
                line = line[:-2]
            case '3':
                curLine = ('\\' + curLine[1: -1] + '|').rjust(width)
                line = line[:-1]
            case _:
                curLine = '|' + curLine[1:-1] + '/'
                line = line[:-1]
    print(curLine)
if len(line) == 1:
    match method:
        case '2':
            print('V'.center(width))
        case '3':
            print('\\'.rjust(width))
        case _:
            print('/')

