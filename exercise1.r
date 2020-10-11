# VECTORS
# 1. Create a vector u that has values: 
#    -10, -9, -8, . . . , 0. 
u <- seq(-10,0)

# 2. Create another vector v that has values: 
#    -0.1, 0.4, 0.9, 1.4, ., and there are 11 terms in v.
v <- seq(-0.1,4.9,by=0.5)

# 3. Calculate the vector of u+v and u*v.
u + v
u * v

# 4. Increase all terms in u by 1, and then take away 20% from all terms in v
u + 1
v * 0.8

# 5. Create a vector w that contains all the numbers from u and then v. Report the length of w.
w <- c(u,v)
length(w)

# 6. Use a command to return the 14th, 15th and 16th value of w. What about the 2nd, the
#    5th, 9th and 21st value of w? What is the 23rd value?
w[14:16]
w[c(2,5,9,21,23)]

# 7. Sort w in the descending order.
sort(w, decreasing=T)



# MATRICES
# 1. Create the following matrix `A`:
#        a  b  c  d  e
#    A   1  3  5  7  9
#    B  11 13 15 17 19
#    C  21 23 25 27 29
#    D  31 33 35 37 39
A <- matrix(seq(1,39,2), 4, 5, byrow=T)
rownames(A) <- c('A','B','C','D')
colnames(A) <- c('a','b','c','d','e')

# 2. Extract a sub-matrix `A_sub` containing columns a and b
A_sub <- A[1:2,1:2]

# 3. Create 3 integer vectors x, y, z each containing 3 elements.
#    Combine the 3 vectors into a 3x3 matrix, where each column 
#    represents a vector. Change the row names to a, b, c.
x <- seq(0,3)
y <- seq(4,6)
z <- seq(7,9)
B <- cbind(x,y,z)  # alt for rows: rbind()
rownames(B) <- c('a','b','c')
colnames(B) <- c('x','y','z')