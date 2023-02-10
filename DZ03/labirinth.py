"""
Волновой алгоритм нахождения кратчайшего пути из лабиринта
"""
import time


def find_path(lab):

    def find_exit():
        for i in range(len(lab[0])):
            if lab[0][i] == ' ':
                return 0, i
            if lab[len(lab) - 1][i] == ' ':
                return len(lab) - 1, i
        for i in range(len(lab)):
            if lab[i][0] == ' ':
                return i, 0
            if lab[i][len(lab[0]) - 1] == ' ':
                return i, len(lab[0]) - 1

    def trace(trace_lab, x, y, step):
        for i in range(len(trace_lab)):
            for j in range(len(trace_lab[0])):
                if trace_lab[i][j] == str(step):
                    if i > 0:
                        if trace_lab[i - 1][j] == ' ':
                            trace_lab[i - 1][j] = str(step + 1)
                    if i < len(trace_lab) - 1:
                        if trace_lab[i + 1][j] == ' ':
                            trace_lab[i + 1][j] = str(step + 1)
                    if j > 0:
                        if trace_lab[i][j - 1] == ' ':
                            trace_lab[i][j - 1] = str(step + 1)
                    if j < len(trace_lab[0]) - 1:
                        if trace_lab[i][j + 1] == ' ':
                            trace_lab[i][j + 1] = str(step + 1)
        if trace_lab[x][y] == ' ':
            return(trace(list(map(lambda x: x, list(map(lambda x: x, trace_lab)))), x, y, step + 1))
        else:
            return(trace_lab)

    x, y = find_exit()
    path = []
    final_lab = trace(list(map(lambda a: a[:], list(map(lambda b: b, lab)))), x, y, 0)
    step_count = int(final_lab[x][y]) + 1
    for i in range(step_count, 0, -1):
        if x > 0:
            if final_lab[x - 1][y] == str(i - 1):
                path.append((1, 0))
                x -= 1
                continue
        if x < len(final_lab) - 1:
            if final_lab[x + 1][y] == str(i - 1):
                path.append((-1, 0))
                x += 1
                continue
        if y > 0:
            if final_lab[x][y - 1] == str(i - 1):
                path.append((0, 1))
                y -= 1
                continue
        if y < len(final_lab[0]) - 1:
            if final_lab[x][y + 1] == str(i - 1):
                y += 1
                path.append((0, -1))
    for i in range(step_count):
        lab[x][y] = '*'
        print('\n'*10)
        print('\n'.join(''.join('\033[31m()\033[0m' if j == '*' else j * 2 for j in k) for k in lab))
        time.sleep(0.5)
        lab[x][y] = ' '
        if len(path) > 0:
            delta = path.pop()
            x = x + delta[0]
            y = y + delta[1]


my_lab = [['X', 'X', 'X', 'X', ' ', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
          ['X', ' ', ' ', 'X', ' ', 'X', ' ', ' ', ' ', 'X', ' ', 'X'],
          ['X', ' ', '0', 'X', ' ', ' ', ' ', 'X', ' ', 'X', ' ', 'X'],
          ['X', ' ', 'X', 'X', 'X', 'X', 'X', 'X', ' ', 'X', ' ', 'X'],
          ['X', ' ', 'X', ' ', ' ', ' ', ' ', 'X', ' ', 'X', ' ', 'X'],
          ['X', ' ', ' ', ' ', ' ', 'X', ' ', ' ', ' ', ' ', ' ', 'X'],
          ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']]

if __name__ == '__main__':
    find_path(my_lab)