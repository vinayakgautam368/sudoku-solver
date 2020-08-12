import numpy as np
grid=[[0,0,0,0,5,0,1,4,0],
     [7,0,0,0,0,8,0,9,0],
     [0,0,5,2,0,0,0,7,0],
     [0,4,0,0,0,0,6,5,9],
     [0,0,0,6,0,2,0,0,0],
     [6,7,3,0,0,0,0,2,0],
     [0,9,0,0,0,1,5,0,0],
     [0,3,0,5,0,0,0,0,8],
     [0,2,7,0,8,0,0,0,0]]


print(np.matrix(grid))
print("input matix:::")
print("\n\n")
def possible( y,x,n):

    for i in range(9):
        if grid[y][i]==n:
            return False
    for j in range(9):
        if grid[j][x]==n:
            return False
    x0=(x//3)*3
    y0=(y//3)*3
    for i in range(3):
        for j in range(3):
            if grid[y0+i][x0+j]==n:
                return False
    return True

def solve():

    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for n in range(1, 10):
                    if possible(y, x, n) :
                        grid[y][x] = n
                        solve()
                        grid[y][x] = 0
                return
    print("output matrix::::")
    print(np.matrix(grid),"\n")



solve()





