'''Create Echelon form of a given matrix and find whether the given matrix is consistent or not and then if it is consistent then find out whether the matrix has unique solution or infinitely many solution...'''

import numpy as np

matrix = np.array([[2, 2, 3], [4, 5, 6], [7, 8, 9]])
print("The matrix formed is :")
print(matrix)
aug_matrix = np.array([[2, 2, 3, 7], [4, 5, 6, 8], [7, 8, 9, 12]])
print("The augmented matrix formed is :")
print(aug_matrix)
# Reducing R2 to get a zero
a = aug_matrix[1][0]/aug_matrix[0][0]
for i in range(0, 4):
    aug_matrix[1][i] = aug_matrix[1][i] - a * aug_matrix[0][i]
for i in range(0, 3):
    matrix[1][i] = matrix[1][i] - a * matrix[0][i]
print("R2 reduced :")
print(aug_matrix)
# Reducing R3 to get a zero
a = aug_matrix[2][0]/aug_matrix[0][0]
for i in range(0, 4):
    aug_matrix[2][i] = aug_matrix[2][i] - a * aug_matrix[0][i]
for i in range(0, 3):
    matrix[2][i] = matrix[2][i] - a * matrix[0][i]
print("R3 reduced :")
print(aug_matrix)
# Reducing R3 to get another zero
a = aug_matrix[2][1]/aug_matrix[1][1]
for i in range(0, 4):
    aug_matrix[2][i] = aug_matrix[2][i] - a * aug_matrix[1][i]
for i in range(0, 3):
    matrix[2][i] = matrix[2][i] - a * matrix[1][i]
print("R3 reduced again to get the Echelon form (Augmented Matrix Echelon form):")
print(aug_matrix)
print("Matrix Echelon form :")
print(matrix)
# Rank of a 3 x 3 matrix is 3
n = 3
rank = 3
rank1 = rank
# Evaluating rank of Echelon matrix
for i in range(0, 3):
    if(matrix[i][0] == 0 and matrix[i][1] == 0 and matrix[i][2] == 0):
        rank = rank - 1
# Evaluating rank of Augmented Echelon matrix
for i in range(0, 3):
    if(aug_matrix[i][0] == 0 and matrix[i][1] == 0 and matrix[i][2] == 0 and matrix[i][3] == 0):
        rank1 = rank1 - 1

# If the ranks of the two matrices are unequal
if(rank != rank1):
    print("The System is inconsistent !!")

# If the rank of the two matrices are equal
if(rank == rank1):
    print("The System is consistent !!")
    # If the number of non-zero rows and the number of unknowns are equal
    if(rank < n):
        print("The System has infinitely many solutions !!")
    else:    # Otherwise
        print("The System has unique set of solutions !!")