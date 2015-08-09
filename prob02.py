def prob2():
    ret = 2
    a1 = 1
    a2 = 2
    for i in xrange(10000):
        an = a1+a2
        a1 = a2
        a2 = an
	if an > 4000000:
            break
	if an%2==0:
            ret += an
    print ret
prob2()
