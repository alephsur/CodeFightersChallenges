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




def makeArrayConsecutive2(statues):
    numberOfStatus = 0
    statues = sorted(statues)
    for i in range(0, len(statues) - 1):
        if (statues[i + 1] - statues[i]) > 1:
            numberOfStatus = numberOfStatus + (statues[i + 1] - (tatues[i]+1))

    return numberOfStatus

statues = [6, 2, 3, 8]

#makeArrayConsecutive2(statues)



def almostIncreasingSequence(sequence):
    changes = 0
    maxValue = -100000000
    secondMax = -100000000
    for i in sequence:
        if i > maxValue:
            secondMax = maxValue
            maxValue = i
        elif i > secondMax:
            maxValue = i
            changes = changes + 1
        else:
            changes = changes + 1

    return changes < 2

var =  [1, 2, 1, 2]


#print(almostIncreasingSequence(var))

def matrixElementsSum(matrix):
    for i in range(0,len(matrix)):
        for j in range(0,len(matrix[0])):
            if matrix[i][j] == 0:
                for k in range(i, len(matrix)):
                    matrix[k][j] = 0
    total = 0
    for i in matrix:
        total = total + sum(i)
    return total

matrix = [[0, 1, 1, 2],
          [0, 5, 0, 0],
          [2, 0, 3, 3]]

print(matrixElementsSum(matrix))


def allLongestStrings(inputArray):
    #return [x for x in inputArray if len(x) == len(max(inputArray, key=len))]
    long = 0
    newArray = []
    for i in inputArray:
        if len(i) > long:
            newArray = []
            newArray.append(i)
            long = len(i)
        elif len(i) == long:
            newArray.append(i)
    return newArray


inputArray = ["aba", "aa", "ad", "vcd", "aba"]


#allLongestStrings(inputArray)


def commonCharacterCount(s1, s2):
    countChars = 0
    for i in s1:
        if i in s2:
            countChars = countChars + 1
            s2=s2.replace(i,"",1)
    return countChars

s1 = "aabcc"
s2 = "adcaa"

#commonCharacterCount(s1,s2)


def isLucky(n):
    #s = str(n)
    #return sum(int(firsthalf) for firsthalf in s[:len(s) // 2]) == sum(int(secondhalf) for secondhalf in s[len(s) // 2:])
    result1 = 0
    result2 = 0
    number = str(n)
    for i in range(0,len(number)):
        if i < len(number )/2:
            result1 = result1 + int(number[i])
        else:
            result2 = result2 + int(number[i])
    return  result1 == result2

#isLucky(1230);




def sortByHeight(a):
    sortList = []
    for i in a:
        if i != -1:
            sortList.append(i)
    sortList = sorted(sortList);
    sortIndex = 0
    for i in range(0,len(a)):
        if a[i] != -1:
            a[i] = sortList[sortIndex]
            sortIndex = sortIndex + 1
    return a




def reverseParentheses(s):
    openParantesis = []
    long = len(s)
    d = 0
    for i in range(0,long):
        if s[i-d] == "(":
            openParantesis.append(i-d)
        if s[i-d] == ")":
            s = s[:openParantesis[-1]] + s[openParantesis[-1]+1:i - d][::-1] + s[i-d + 1:]
            openParantesis.pop()
            d = d + 2

    return s

s = "abc(cba)ab(bac)c"
#s =  "The ((quick (brown) (fox) jumps over the lazy) dog)"
reverseParentheses(s)



