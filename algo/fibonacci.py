__author__ = 'CoesseWa'

i = 2
n = 22
last_fib = 1
before_last = 0


if n == 0:
    print 0
if n == 1:
    print 1

while (i <= n):
    x = last_fib + before_last
    before_last = last_fib
    last_fib = x

    i += 1


print last_fib
