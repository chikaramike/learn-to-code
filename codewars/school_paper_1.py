def paperwork(n, m):
    if n < 0 or m < 0:
        return 0
    else:
        return n * m

print(paperwork(2, 5))
print(paperwork(-2, 5))
