from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = new_matrix()

matrix = [[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12],[13, 14, 15, 16]]
print("\nMATRIX 1:")
print_matrix(matrix)

print("\nMATRIX 2:")
matrix2 = [[10, 15, 0, 1], [15, 20, 0, 1], [20, 25, 0, 1],[0, 0, 0, 1]]
print_matrix(matrix2)

print("\nTesting ident on matrix1:")
ident(matrix)
print_matrix(matrix)

draw_lines( matrix, screen, color )
#display(screen)
