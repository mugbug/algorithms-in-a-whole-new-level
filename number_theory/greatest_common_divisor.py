def gcd(a, b):
    minimun = min([a,b])
    # ...

def euclid(a, b):
    return a if b == 0 else euclid(b, a % b)

print(euclid(13, 23))