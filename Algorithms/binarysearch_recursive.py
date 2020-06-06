def binarysearch_rec(A, key, low, high):
    '''Binary search always in sorted formated.'''
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if key == A[mid]:
            return True
        elif key < A[mid]:
            return binarysearch_rec(A, key, low, mid-1)
        else:
            return binarysearch_rec(A, key, mid+1, high)


A = [12, 23, 34, 56, 67]
high = len(A)
low = 0
print(binarysearch_rec(A, 12, low, high))