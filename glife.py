import random

def grid_size(rows,col):
    board=[]
    for i in range(rows):
        board.append([])
        for j in range(col):
            board[i].append(random.randint(0, 1))
    return board


def display_grid(a):
    strng=""
    for i in a:
        for j in i:
            strng+=f'{j} '
        strng+='\n'
    return strng


print(grid_size(3,3))

    
