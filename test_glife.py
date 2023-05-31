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

# def test_random_input():

