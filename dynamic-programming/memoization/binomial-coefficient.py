
def binom(n, k):
    if k == 0 or k == n:
        return 1
    else:
        MEMO[n][k] = binom(n - 1, k - 1) + binom(n - 1, k)
    return MEMO[n][k]

MAX = 10
NIL = -1

if __name__ == '__main__':
    # initialize memoization matrix with NIL
    MEMO = [[NIL]*MAX]*MAX

    # print first MAX lines of Pascal's Triangle
    for n in range(MAX):
        print_arr = []
        for k in range(n+1):
            print(binom(n, k), ' ', end = '')
        print()