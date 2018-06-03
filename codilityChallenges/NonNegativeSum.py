def solution(A):

    maxSum = 0
    numElemsI = 0
    numElemsJ = 0
    numElemsK = 0
    sumaI=0
    sumaJ=0
    sumaK = 0

    for i in range(0,len(A)):
        sumaI = sumArray(A[i:])
        sumaJ = sumArray(A[:len(A)-i])
        #sumaK = sumArray(A[i:len(A)-i])

        if sumaI >= 0:
            if numElemsI <  len(A[i:]):
                numElemsI = len(A[i:])
        if sumaJ >= 0:
            if numElemsJ < len(A[:len(A)-i]):
                numElemsJ = len(A[:len(A)-i])

        sumaI = sumaI

        if sumaK >= 0:
            if numElemsK < len(A[i:len(A)-i]):
                numElemsK = len(A[i:len(A)-i])

    maxCount = max(numElemsI,numElemsJ,numElemsK)

    print(A)
    return maxCount


def sumArray(array):
    suma = 0
    for i in range(0,len(array)):
        suma = suma + array[i]
    return suma

a = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1]


print(solution(a))