def prime_decomp(n):
    table = []
    i = 2
    while i*i <= n:
        while n%i==0:
            n /= i
            table.append(i)
        i += 1
    if n > 1:
        table.append(n)
    return table

def prob3():
    #素因数分解                                                                 
    X = 600851475143
    table = prime_decomp(X)
    print table[-1]

prob3()
