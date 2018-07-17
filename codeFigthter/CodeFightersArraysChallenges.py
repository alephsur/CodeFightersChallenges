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



def removeKFromList(l, k):
    list = ListNode(0)
    temp = list
    while l != None:
        if l.value != k:
            temp.next = l
            temp = temp.next
        l = l.next
    temp.next = None
    return list.next

def isListPalindrome(l):
    list = ListNode(0)
    listaNumber = []
    while l != None:
        listaNumber.append(l.value)
        l = l.next
    ## listaNumber == listaNumber[::-1]
    for i in range(0,len(listaNumber)/2):
        if listaNumber[i] != listaNumber[-i-1]:
            return False
    return True

class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None

list = ListNode(3)
list.next = ListNode(1)
second = list.next
second.next = ListNode(2)
third = second.next
third.next = ListNode(3)
fourth = third.next
fourth.next = ListNode(4)
fifth = fourth.next
fifth.next = ListNode(5)

k = 3

removeKFromList(list,k)





def addTwoHugeNumbers(a, b):
    number1 = []
    number2 = []
    numberAdd = []
    while a != None:
        number1.append(str(a.value).rjust(4, "0"))
        a = a.next
    while b != None:
        number2.append(str(b.value).rjust(4, "0"))
        b = b.next

    number1 = "".join(number1)
    number2 = "".join(number2)
    total = int(number1) + int(number2)
    if len(str(total))%4 != 0:
        total = str(total).rjust(len(str(total)) + 4 - (len(str(total))%4),'0')
    else:
        total = str(total)
    numero = ""
    for i in range(0, len(total)+1):
        if i % 4 == 0 and i > 0:
            numberAdd.append(int(numero[::-1]))
            if i < len(total):
                numero = ""
                numero = numero + total[-i - 1]
        else:
            numero = numero + total[-i-1]

    return numberAdd[::-1]



list = ListNode(9876)
list.next = ListNode(5432)
second = list.next
second.next = ListNode(1999)

third = ListNode(1)
third.next = ListNode(8001)
#fourth = third.next
#fourth.next = ListNode(100)

print (addTwoHugeNumbers(list,third))


def mergeTwoLinkedLists(l1, l2):
    l3 = ListNode(0)
    temp = l3
    while l1 != None or l2 != None:
        if l1 == None:
            temp.next = l2
            temp = temp.next
            l2 = l2.next
            continue
        if l2 == None:
            temp.next = l1
            temp = temp.next
            l1 = l1.next
            continue
        if l1.value <= l2.value:
            temp.next = l1
            temp = temp.next
            l1 = l1.next
            continue
        if l1.value > l2.value:
            temp.next = l2
            temp = temp.next
            l2 = l2.next
            continue
        temp.next = ListNode(0)
    return l3.next









