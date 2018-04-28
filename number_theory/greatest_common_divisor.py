# O(min(a, b))
def gcd_trivial(a, b):
    minimun = min([a,b])
    gcd = 0
    for i in range(1, minimun+1):
        if (a % i) == 0 and (b % i) == 0:
            gcd = i
    return gcd


# O(log(min(a, b)))
def euclid(a, b):
    return a if b == 0 else euclid(b, a % b)

if __name__ == '__main__':
    print('Trivial:', gcd_trivial(30, 15))
    print('Euclid:', euclid(41232, 512))