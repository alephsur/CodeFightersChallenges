

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

#isCryptSolution(crypt, solution)



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

#removeKFromList(list,k)





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

#print (addTwoHugeNumbers(list,third))


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

#print(matrixElementsSum(matrix))


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
#reverseParentheses(s)

def reverseNodesInKGroups(l, k):
    listOriginal = []

    while l != None:
        listOriginal.append(l.value)
        l = l.next

    listReversed = []
    for i in range(0, len(listOriginal), k):
        j = i + k
        sublist = listOriginal[i:j]
        if len(sublist) < k:
            listReversed += sublist[:]
        else:
            listReversed += sublist[::-1]

    return listReversed

list = ListNode(1)
list.next = ListNode(2)
second = list.next
second.next = ListNode(3)
third = second.next
third.next = ListNode(4)
fourth = third.next
fourth.next = ListNode(5)

#reverseNodesInKGroups(list,1)


def alternatingSums(a):
    #return [sum(a[::2]), sum(a[1::2])]
    sum1 = 0
    sum2 = 0
    for i, n in a:
        if i % 2 == 0:
            sum1 = sum1 + n
        else:
            sum2 = sum2 + n
    return [sum1,sum2]

a = [50, 60, 60, 45, 70]

#alternatingSums(a)


def addBorder(picture):
    #l=len(picture[0])+2
    #return ["*"*l]+[x.center(l,"*") for x in picture]+["*"*l]
    resultMatrix = []
    long = len(picture[0]) + 2

    resultMatrix.append("*"*long)
    for i in range(len(picture)):
        resultMatrix.append("*" + picture[i] + "*")

    resultMatrix.append("*" * long)
    return resultMatrix


def areSimilar(a, b):
    countChanges = 0

    for i in range(0,len(a)):
        if a[i] != b[i]:
            if countChanges == 1:
                return False
            sw = 0
            if (i+1) < len(a):
                for j in range(i + 1,len(a)):
                    if a[i] == b[j]:
                        sw = 1
                        aux = b[j]
                        b[j] = b[i]
                        b[i] = aux
                    if sw == 1 and countChanges == 0:
                        countChanges = 1
                        break
                if countChanges == 0:
                    return False
                if sw == 0:
                    return False
            else:
                return False
    return True


a = [832, 998, 148, 570, 533, 561, 894, 147, 455, 279]
b = [832, 570, 148, 998, 532, 561, 533, 147, 894, 279]


##print(areSimilar(a,b))

def arrayChange(inputArray):
    countChanges = 0
    for i in range(len(inputArray)):
        if i < len(inputArray)-1:
            if inputArray[i] < inputArray[i+1]:
                continue
            else:
                countChanges = countChanges + (inputArray[i] - inputArray[i+1])+1
                if inputArray[i] == inputArray[i+1]:
                    inputArray[i + 1] = inputArray[i+1] +1
                else:
                    inputArray[i+1] = inputArray[i+1] + (inputArray[i] - inputArray[i+1])+1
        else:
            return countChanges
    return countChanges



#inputArray = [-1000, 0, -2, 0]
#print(arrayChange(inputArray))



def palindromeRearranging(inputString):
    inputString = sorted(inputString)
    countNotDuplicateChar = 0
    while(len(inputString) > 0):
        if len(inputString) >= 2:
            if inputString[0] == inputString[1]:
                inputString.remove(inputString[0])
                inputString.remove(inputString[0])
                continue
            else:
                if countNotDuplicateChar == 1:
                    return False
                countNotDuplicateChar = countNotDuplicateChar + 1
                inputString.remove(inputString[0])
        else:
            if countNotDuplicateChar == 0:
                return True
            else:
                return False
    return True



#inputString =  "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaabc"
#print(palindromeRearranging(inputString))




import re

def isIPv4Address(inputString):
    pat = re.compile("^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$")
    test = pat.match(inputString)
    if test:
        return True
    else:
        return False



print (isIPv4Address("192.168.142.122"))














