from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = new_matrix()

matrix = [[0, 10, 15, 1], [0, 15, 20, 1], [15, 20, 0, 1],[0, 0, 0, 1]]
print("\nMATRIX 1:")
print_matrix(matrix)

print("\nMATRIX 2:")
matrix2 = [[1, 0, 0, 0],[0, 1, 0, 0],[0, 0, 1, 0],[0, 0, 0, 1]]
print_matrix(matrix2)

draw_lines( matrix, screen, color )
#display(screen)
