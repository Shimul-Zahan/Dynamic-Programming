def sum(n):
    
    # base case
    if n== 0:
        return 0
    # recursion call
    return n + sum(n - 1)

print(sum(5))

# Factorial

def factor(n):
    # base case
    if n==0:
        return 1
    # recursion call
    return n * factor(n-1)

print(factor(4))


# Factorial using tail recursion but not using backtracking

def factor(n, accumulator):

    # base case
    if n==0:
        return accumulator
    # recursion call
    return factor(n - 1, n*accumulator)

print(factor(10, 1))