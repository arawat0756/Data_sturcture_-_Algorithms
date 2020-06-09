def shellsort(A, high):
    interval = high//2
    while interval  > 0:
        for i in range(interval, high):
            temp = A[i]
            j = i
            while j >= interval and A[j - interval] > temp:
                A[j] = A[j - interval]
                j -= interval
                
            A[j] = temp
        interval //=2



A = [84, 21, 96, 15, 47]
print('Orignal Array : ', A)
shellsort(A, len(A))
print("Sorted Array : ", A)