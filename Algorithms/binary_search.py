def binary_search(A, key):
    '''Binary search always in sorted formated.'''
    low = 0
    high = len(A)-1
    while low <= high:
        mid = (low + high) // 2
        if key == A[mid]:
            return f"{key} Found"
        elif key < A[mid]:
            high = mid -1
        else:
            low = mid +1
    return f"{key} Not Found"
    

A = [15,21,32,45,50]
print(binary_search(A, 32))
print(binary_search(A, 90))