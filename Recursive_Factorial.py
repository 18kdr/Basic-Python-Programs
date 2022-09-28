def recursive_fact(n):
    if n == 1:
        return n
    else:
        temp = recursive_fact(n-1)
        temp = temp * n
        return temp

print(recursive_fact(6))


# Recursive factorial is used to iterate the numbers in the backward order
# ex: 1 * 2 * 3 * 4 * 5