# tip: i & (-i) returns the least bit 1

# stackoverflow explanation, for i = 44
# i           = 0000 0000 0000 0000 0000 0000 0010 1100
# ~i          = 1111 1111 1111 1111 1111 1111 1101 0011
# -i = (~i)+1 = 1111 1111 1111 1111 1111 1111 1101 0100
# (i) & (-i)  = 0000 0000 0000 0000 0000 0000 0000 0100

def construct_bit(arr, n):
    # constructs and returns a BIT for a
    # given array 'arr' of size 'n'
    for index in range(n):
        update(index, arr[index])

def get_sum(index):
    # returns the sum of 'arr' elements
    ans = 0
    index += 1
    while index > 0:
        ans += bit[index]
        index -= index & (-index)
    return ans

def update(index, val):
    # updates BIT at given index with given value 'val'
    index += 1
    while index <= len(arr):
        bit[index] += val
        index += index & (-index)
        # same as
        # index += index & (~index + 1)

if __name__ == '__main__':
    arr = [3, 2, -1, 6, 5, 4, -3]
    bit = [0]*(len(arr)+1)
    construct_bit(arr, len(arr))
    update(2, 6)
    print(bit)