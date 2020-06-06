def linear_search(A, key):
    '''The time complexity is O(n)'''
    index = 0
    while index < len(A):
        if A[index] == key:
            return f"Key: {key}, Index: {index} found" 
        index = index + 1
    return f"Key not found"


A = [84, 56, 32, 45, 89]
print(linear_search(A, 21))    
print(linear_search(A, 45))    
    