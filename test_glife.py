import glife

def test_display_grid():
    assert glife.display_grid([["#","#","#"],["#","#","#"],["#","#","#"]]) == """# # # 
# # # 
# # # 
"""


def test_display_alive():
    expected_output = '1 1 1 1 1 \n1 1 1 1 1 \n1 1 1 1 1 \n1 1 1 1 1 \n1 1 1 1 1 \n'
    assert glife.display_grid([[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]]) == expected_output