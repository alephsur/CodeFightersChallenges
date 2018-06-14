def opt_first_duplicate(arr):
    unique_nb = set()
    for nb in arr:
        if nb in unique_nb:
            return nb
        else:
            unique_nb.add(nb)
    return -1

#a = [2, 1, 3, 5, 3, 2]

#print(opt_first_duplicate(a))

def firstNotRepeatingCharacter(s):
    unique_char = list()
    remove_elements = list()
    for charElem in s:
        if charElem in unique_char:
            unique_char.pop(unique_char.index(charElem))
            remove_elements.append(charElem)
        else:
            if charElem not in remove_elements:
                unique_char.append(charElem)

    if len(unique_char) > 0:
        return list(unique_char)[0]
    else:
        return '_'

#s = "abacabad"

#print(firstNotRepeatingCharacter(s))

def rotateImage(a):
    matrix = []
    for i in range(len(a)):
        vector = []
        for j in range(len(a)):
            vector.append(a[j][i])
        vector.reverse()
        matrix.append(vector)
    return matrix

#a = [[1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]]

#print(rotateImage(a))



def sudoku2(grid):
    for i in range(len(grid)):
        rowValues = list()
        colValues = list()

        for j in range(len(grid)):
            if grid[i][j] in rowValues or grid[j][i] in colValues:
                return False
            else:
                if grid[i][j].isdigit():
                    rowValues.append(grid[i][j])
                if grid[j][i].isdigit():
                    colValues.append(grid[j][i])
            if j % 3 == 0 and i % 3 == 0:
                internSquares = list()
                for h in range(3):
                    for k in range(3):
                        if grid[i+h][j+k] in internSquares:
                            return False
                        else:
                            if grid[i+h][j+k].isdigit():
                                internSquares.append(grid[i+h][j+k])
    return True



#grid = [ [".",".",".",".",".",".","5",".","."],
#         [".",".",".",".",".",".",".",".","."],
#         [".",".",".",".",".",".",".",".","."],
#         ["9","3",".",".","2",".","4",".","."],
#         [".",".","7",".",".",".","3",".","."],
#         [".",".",".",".",".",".",".",".","."],
#         [".",".",".","3","4",".",".",".","."],
#         [".",".",".",".",".","3",".",".","."],
#         [".",".",".",".",".","5","2",".","."]]


#print(sudoku2(grid))


def isCryptSolution(crypt, solution):
    charValues = dict(solution)
    valuesToSum = []
    for i in range(len(crypt)):
        valueToAppend = ''
        for j in range(len(crypt[i])):
            valueToAppend = valueToAppend + charValues[crypt[i][j]]
        valuesToSum.append(valueToAppend)

    if int(valuesToSum[0]) + int(valuesToSum[1]) != int(valuesToSum[2]):
        return False
    else:
        if len(valuesToSum[0]) > 1 and valuesToSum[0][0] == '0':
            return False
        if len(valuesToSum[0]) > 1 and valuesToSum[1][0]=='0':
            return False
        if len(valuesToSum[0]) > 1 and valuesToSum[2][0]=='0':
            return False
        else:
            return True

crypt = ["TEN",
 "TWO",
 "ONE"]

solution = [["O","1"],
 ["T","0"],
 ["W","9"],
 ["E","5"],
 ["N","4"]]

isCryptSolution(crypt, solution)






















