def calculate_rec(n):
    '''This function also called tail recursion.'''
    if n > 0:
        k = n ** 2
        print(k)
        calculate_rec(n - 1)

calculate_rec(4)


# def calculate_rec(n):
#     '''This function is called head recursion'''
#     if n > 0:
#         calculate_rec(n - 1)
#         k = n ** 2
#         print(k)
        

# calculate_rec(4)