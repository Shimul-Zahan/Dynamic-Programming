# using recursion
def gcd(a,b):
    # base case
    if a % b == 0:
        return b
    return gcd(b, a%b)

print(gcd(24, 9))

# using iteration
def gcd(a, b):
    while a % b != 0:
        a, b = b, a%b
    return b

print(gcd(24, 9))