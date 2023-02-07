# - Transform all the three given lists into numpy arrays.
# - Transform the L1 array into a matrix (called L5) with 9 lines and 3 columns.
# - Print the obtained matrix (L5). You can find a example of the desired matrix in the document Ex_3_array_new_shape_V2.txt
# - Reshape the arrays L2 and L3 into 1 columns arrays and create a 2 columns matrix (called L6) where the first column is the L2 array and the second the L3 array.
# - Print the obtained matrix (L6). You can find a example of the desired matrix in the document Ex_3_array_matrix_V2.txt
# - Do the multiplication of L3 by 5 and call it L7.
# - Print the obtained array (L7). You can find a example of the desired matrix in the document Ex_3_array_operation_V2.txt

import numpy as np

L1 = [51, 16, 56, 10, 31, 1, 1, 55, 6, 27, 30, 36, 9, 17, 30, 48, 47, 5, 31, 12, 18, 47, 25, 6, 29, 48, 44]
L2 = [44, 31, 3, 8, 52, 20, 51, 26, 53, 38, 16, 23, 53, 49, 26, 23, 23, 16, 35, 2, 14, 7, 6, 25, 38, 21, 26]
L3 = [42, 6, 31, 30, 9, 58, 50, 51, 37, 36, 6, 57, 43, 9, 49, 13, 20, 41, 36, 35, 31, 38, 35, 46, 15, 53, 52]
L4 = np.array(L3.copy())


L5 = np.array(L1).reshape(9, 3)
L2 = np.array(L2).reshape(-1, 1)
L3 = np.array(L3).reshape(-1, 1)

L6 = np.hstack([L2, L3])


L7 = np.array(5 * L3)
l7 = 5 * L4

# Here are the print function for each matrix:
print(L5)
print(L6)
print(L7)
print(l7)