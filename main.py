from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = []#new_matrix()

print("Testing add_edge and add_point: (1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12)")
add_edge(matrix, 1.00, 2.00, 3.00, 4.00, 5.00, 6.00)
add_point(matrix, 7.00, 8.00, 9.00)
add_point(matrix, 10.00, 11.00, 12.00)

#matrix = [[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12],[13, 14, 15, 16]]
print("\nMATRIX 1:")
print_matrix(matrix)

print("\nMATRIX 2:")
matrix2 = [[10.00, 15.00, 0.00, 1.00], [15.00, 20.00, 0.00, 1.00], [20.00, 25.00, 0.00, 1.00],[0.00, 0.00, 0.00, 1.00]]
print_matrix(matrix2)

print("\nTesting ident on matrix1:")
ident(matrix)
print_matrix(matrix)

print("\nTesting matrix_mult:")
matrix_mult(matrix, matrix2)
print_matrix(matrix2)

print("\nTesting matrix_mult (scaling by 2):")
matrix = [[2.00, 0.00, 0.00, 0.00],[0.00, 2.00, 0.00, 0.00],[0.00, 0.00, 2.00, 0.00],[0.00, 0.00, 0.00, 2.00]]
#print_matrix(matrix)
matrix_mult(matrix,matrix2)
print_matrix(matrix2)

print("\nTesting matrix mult:")
matrix = [[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12],[13, 14, 15, 16]]
print_matrix(matrix)
print("\n")
matrix2 = [[10.00, 15.00, 0.00, 1.00], [15.00, 20.00, 0.00, 1.00], [20.00, 25.00, 0.00, 1.00],[0.00, 0.00, 0.00, 1.00]]
print_matrix(matrix2)
print("\n")
matrix_mult(matrix, matrix2)
print_matrix(matrix2)

draw_lines( matrix, screen, color )
#display(screen)
