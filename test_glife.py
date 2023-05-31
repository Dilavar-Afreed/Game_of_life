import glife

def test_display_grid():
    assert glife.display_grid([["#","#","#"],["#","#","#"],["#","#","#"]]) == """# # # 
# # # 
# # # 
"""

def test_display_alive():
    assert glife.display_grid([[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]]) == '# # # # # \n# # # # # \n# # # # # \n# # # # # \n# # # # #'

                          
                                                                              