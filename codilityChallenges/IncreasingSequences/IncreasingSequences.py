def solution(A,B):
    numberSwaps = 0
    aux = 0
    swapped = False
    if len(A) != len(B):
        return -1
    if len(A) >= 2:
        for i in range(1,len(A)):
            if A[i] <= A[i-1]:
                if B[i]>A[i-1] and A[i] > B[i-1]:
                    aux = A[i]
                    A[i] = B[i]
                    B[i] = aux
                    numberSwaps+=1
                else:
                    return -1
            else:
                if B[i] <= B[i-1]:
                    if A[i]>B[i-1] and B[i]>A[i-1]:
                        aux = A[i]
                        A[i] = B[i]
                        B[i] = aux
                        numberSwaps+=1
                    else:
                        return -1
        return numberSwaps
    else:
        return -1


a=[-13, -12, 0, -6, 5, 9, 12, 4, 18, 8]
b=[-15, -4, -7, 3, -5, -4, 0, 17, 7, 25]


print(solution(a,b))



















