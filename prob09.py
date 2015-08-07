A, B, C = 0, 0, 0
for a in xrange(1, 1000/3):
    for b in xrange(a+1, (1000-a)/2-1):
        c = 1000 - (a+b)
        left = a*a + b*b
        right = c*c
        if left == right:
            A, B, C = a, b, c
            break
        elif left > right:
            break
print A*B*C
