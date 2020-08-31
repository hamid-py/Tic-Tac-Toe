x_o = list('_________')
x_o_dict = {}
win = {'count': 0, 'winner': None}
quit = {'end': True}
move_list = [[7, 4, 1], [8, 5, 2], [9, 6, 3]]


def correct_input(x):
    if not x.isdigit():
        raise ValueError
    if not (1 <= int(x) <= 3):
        raise EOFError
    else:
        return int(x)


def check_ocupy(x, y):
    if not x_o_dict[move_list[x - 1][y - 1]] == '_':
        raise OverflowError

    else:
        return True


def check_turn(x_o_dict):
    x = 0
    y = 0
    for i in x_o_dict:
        if x_o_dict[i] == 'X':
            x += 1
        elif x_o_dict[i] == 'O':
            y += 1
    if x == y:
        return 'X'
    return 'O'


def check_impossible(a):
    win['winner'] = a
    win['count'] += 1


def print_x_o(x_o_dict):
    print('---------')
    print('|', x_o_dict[1], x_o_dict[2], x_o_dict[3], '|')
    print('|', x_o_dict[4], x_o_dict[5], x_o_dict[6], '|')
    print('|', x_o_dict[7], x_o_dict[8], x_o_dict[9], '|')
    print('---------')


def check_finish(x_o_dict):
    if x_o_dict[1] == x_o_dict[2] == x_o_dict[3] != '_':
        check_impossible(x_o_dict[1])
    if x_o_dict[4] == x_o_dict[5] == x_o_dict[6] != '_':
        check_impossible(x_o_dict[4])
    if x_o_dict[7] == x_o_dict[8] == x_o_dict[9] != '_':
        check_impossible(x_o_dict[7])
    if x_o_dict[1] == x_o_dict[4] == x_o_dict[7] != '_':
        check_impossible(x_o_dict[1])
    if x_o_dict[2] == x_o_dict[5] == x_o_dict[8] != '_':
        check_impossible(x_o_dict[5])
    if x_o_dict[3] == x_o_dict[6] == x_o_dict[9] != '_':
        check_impossible(x_o_dict[6])
    if x_o_dict[1] == x_o_dict[5] == x_o_dict[9] != '_':
        check_impossible(x_o_dict[5])
    if x_o_dict[3] == x_o_dict[5] == x_o_dict[7] != '_':
        check_impossible(x_o_dict[5])
    if win['count'] == 1 and win['winner'] != '_':
        print(f'{win["winner"]} wins')
        quit['end'] = False
    elif win['count'] == 0 and '_' not in x_o_dict.values():
        print('Draw')
        quit['end'] = False
    # elif win['count'] > 1:
    #     print('Impossible')
    # elif not (x_o.count('X') == x_o.count('O') or x_o.count('X') == x_o.count('O') + 1):
    #     print('Impossible')
    # elif '_' in x_o:
    #     print('Game not finished')


for i in range(len(x_o)):
    x_o_dict[i + 1] = x_o[i]

print_x_o(x_o_dict)
check_finish(x_o_dict)

while quit['end']:
    try:
        x, y = input('Enter the coordinates:').split()
        x = correct_input(x)
        y = correct_input(y)
        check_ocupy(x, y)
        turn = check_turn(x_o_dict)
        x_o_dict[move_list[x - 1][y - 1]] = turn
        print_x_o(x_o_dict)
        check_finish(x_o_dict)
    except ValueError:
        print('You should enter numbers!')
    except OverflowError:
        print('This cell is occupied! Choose another one!')
    except EOFError:
        print('Coordinates should be from 1 to 3!')
