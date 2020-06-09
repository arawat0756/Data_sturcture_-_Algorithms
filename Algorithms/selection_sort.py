def selectionsort(A):
    for i in range(len(A)-1, 0, -1):
        max_positon = 0
        for j in range(1, i+1):
            if A[j] > A[max_positon]:
                max_positon = j
        temp = A[i]
        A[i] = A[max_positon]
        A[max_positon] = temp

A = [84, 21, 96, 15, 47]
print('Orignal Array : ', A)
selectionsort(A)
print("Sorted Array : ", A)
