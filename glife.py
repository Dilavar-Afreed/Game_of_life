

def grid_size(rows,col):
    board=[]
    for i in range(rows):
        board.append([])
        for j in range(col):
            board[i].append(None)
    return board

def display_grid(a):
    strng=""
    for i in a:
        for j in i:
            strng+=f'{j} '
        strng+='\n'
    return strng


    
    
    
