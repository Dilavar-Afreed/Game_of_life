import glife



def test_grid_size():
    board = glife.grid_size(3, 3)
    assert len(board) ==3
    assert len(board[0]) == 3

def test_display_grid():
    assert glife.display_grid([["#","#","#"],["#","#","#"],["#","#","#"]]) == """# # # 
# # # 
# # # 
"""


def test_display_alive():
    expected_output = '1 1 1 1 1 \n1 1 1 1 1 \n1 1 1 1 1 \n1 1 1 1 1 \n1 1 1 1 1 \n'
    assert glife.display_grid([[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]]) == expected_output


def test_get_neighbours():
    board = [[0, 1, 0], [1, 1, 0], [0, 0, 1]]
    assert glife.get_neighbours(board, 0, 0) == 3
    assert glife.get_neighbours(board, 0, 1) == 2
    assert glife.get_neighbours(board, 0, 2) == 2
    assert glife.get_neighbours(board, 1, 0) == 2
    assert glife.get_neighbours(board, 1, 1) == 3
    assert glife.get_neighbours(board, 1, 2) == 3
    assert glife.get_neighbours(board, 2, 0) == 2
    assert glife.get_neighbours( board,2, 1) == 3
    assert glife.get_neighbours(board, 2, 2) == 1
    

    



# def test_update():
#     grid=[[1,1,0],[1,0,0],[0,1,0]]
#     expected_output="1 1 0/n1 0 0/n1 0 0"
#     assert glife.update_grid(grid) == expected_output

# def test_random_input():

