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




    



 
def get_neighbours(grid, row, col):
    live_neighbor_count = 0
    for i in range(row-1, row+2):
        for j in range(col-1, col+2):
            if (i == row and j == col) or i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
                continue
            if grid[i][j] == 1:
                live_neighbor_count += 1
    return live_neighbor_count




# if __name__=="__main__":
#     row=3
#     col=3
#     board=grid_size(row,col)
#     # print(display_grid(board))
#     print(board)


 

    
