#coding: utf-8                                                                  

N = 20
table = [1 for i in xrange(N+1)]
for j in xrange(N):
    for i in xrange(N):
        table[i+1] = table[i]+table[i+1]
print table[-1]
