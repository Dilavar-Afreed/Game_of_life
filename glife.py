def display_grid(a):
    strng=""
    for i in a:
        for j in i:
            strng+=f'{j} '
        strng+='\n'
    return strng

    
    
    
    
# print(display_grid([[1,2,3],[1,2,3],[1,2,3]]))