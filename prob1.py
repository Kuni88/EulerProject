#coding: utf-8
def prob1():
    ret = 0
    for i in xrange(1, 1000):
        if i%3==0 or i%5==0:
            ret += i
    print ret

if __name__ == '__main__':
  prob1()
