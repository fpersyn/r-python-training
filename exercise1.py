import numpy as np
import pandas as pd  # numpy array indexing

# VECTORS
# 1. Create a vector u that has values: 
#    10, -9, -8, . . . , 0. 
u = np.arange(-10,1)

# 2. Create another vector v that has values: 
#    -0.1, 0.4, 0.9, 1.4, ., and there are 11 terms in v.
v = np.arange(-0.1, 5.0, 0.5)

# 3. Calculate the vector of u+v and u*v.
u + v
u * v

# 4. Increase all terms in u by 1, and then take away 20% from all terms in v
u = u + 1
v = v * 0.8

# 5. Create a vector w that contains all the numbers from u and then v. 
#    Report the length of w.
w = np.concatenate([u,v])
w.size  # alt for n x m: w.shape

# 6. Use a command to return the 14th, 15th and 16th value of w. What about the
#    2nd, the 5th, 9th and 21st value of w? What is the 23rd value?
w[13:16]
w[[1,4,8,20]]  # Adding 22 will result in an IndexError (out of bounds)

# 7. Sort w in the descending order.
np.sort(w)[::-1]  # We add [::1] to reverse the sorted array.



# MATRICES
# 1. Create the following matrix `A`:
#        a  b  c  d  e
#    A   1  3  5  7  9
#    B  11 13 15 17 19
#    C  21 23 25 27 29
#    D  31 33 35 37 39
pd.DataFrame(np.arange(1,40,2).reshape((4,5)),
            index=['A','B','C','D'],
            columns=['a','b','c','d','e'])

# 2. Extract a sub-matrix `A_sub` containing columns a and b
A_sub = A.iloc[:,1:3]

# 3. Create 3 integer vectors x, y, z each containing 3 elements.
#    Combine the 3 vectors into a 3x3 matrix, where each column
#    represents a vector. Change the row names to a, b, c.
x = np.arange(1,4)
y = np.arange(4,7)
z = np.arange(7,10)
B = pd.DataFrame(np.column_stack([x,y,z]),  # alt for rows: np.stack()
				 index=['a','b','c'],
				 columns=['x','y','z'])