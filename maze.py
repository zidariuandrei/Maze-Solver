board = [
    [1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,0,0,1],
    [1,0,1,1,1,0,1,0,1],
    [1,0,1,0,1,0,0,0,1],
    [1,0,0,0,1,0,1,1,1],
    [1,0,1,1,1,0,0,0,1],
    [1,0,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,0,0,3],
    [1,2,1,1,1,1,1,1,1]
]

def findStart (bo) :
    for i in range(len(bo)):
        for j in range (len(bo[0])):
            if bo[i][j] == 2:
                return (i, j)

def checkEnd(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 3:
                return (i, j)

def isValid(bo, pos):
    row = pos[0]
    column = pos[1]
    #check up
    if bo[row-1][column] == 0 or bo[row-1][column] == 3 or bo[row-1][column] != "x" and row==0 :
        return (row-1, column)
    #check down
    
    elif  bo[row+1][column] ==0 or bo[row+1][column] ==3 or bo[row+1][column] !="x" and row==8 :
        return (row+1, column)
    #check left

    elif  bo[row][column-1] ==0 or bo[row][column-1] ==3 or bo[row][column-1] !="x" and column==0:
        return (row, column-1)
    #check right
    elif  bo[row][column+1] ==0 or bo[row][column+1] ==3 or bo[row][column-1] !="x" and column==8:
        return (row, column+1)
    else: 
        return False 

def solve(bo, position):
    check= checkEnd(bo)
    if not check :
        return True
    else:
        pos = isValid(bo, position)
        for i in range(2):
            if pos:
                row,column = pos
                bo[row][column]= "-"
            
                if solve(bo, pos):
                    return True
                bo[row][column] = "x"
        
        return False 

def printBoard(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0 or bo[i][j] == "x" :
                print(" ", end=" ")
            else:
                print(bo[i][j], end="")
                print(" ", end="")
        print("")
    print("")

printBoard(board)
find= findStart(board)
solve(board, find)
printBoard(board)