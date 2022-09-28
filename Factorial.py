def iterative_function(n):
    fact = 1
    for i in range(2,n + 1):
        fact *= i
    return fact

print(iterative_function(6))

# 5 * 4 * 3 * 2 * 1
#faster than the recursive iterative method