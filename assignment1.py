def homework(a):
    result = a[(a % 5 == 0) & (a % 2 == 1)]
    return result