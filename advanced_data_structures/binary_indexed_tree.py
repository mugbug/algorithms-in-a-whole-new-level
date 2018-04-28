def construct_bit(arr, n):
    # constructs and returns a BIT for a
    # given array 'arr' of size 'n'

    # - step 1:
    #   root index = 0 (always with value 0 as well)
    # - step 2:
    #   subsequent nodes' parents will be
    #       current node binary index with rightest 1 cleared
    for index in range(n):
        pass

def get_sum(index):
    # returns the sum of 'arr' elements
    pass

def update(index, val):
    # updates BIT at given index with given value 'val'
    i = 0  
    pass

arr = [3, 2, -1, 6, 5, 4, -3]
bit = [0]*(len(arr)+1)
construct_bit(arr, len(arr))