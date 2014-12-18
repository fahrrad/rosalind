__author__ = 'CoesseWa'

from collections import deque


n = m = 0
A = B = []


with open('rosalind_merge_sort.txt', 'rt') as f:
    n = int(f.readline().strip())
    A = deque(map(int, f.readline().strip().split(' ')))

    m = int(f.readline().strip())
    B = deque(map(int, f.readline().strip().split(' ')))

print n, A
print m, B

C = []
while len(A) or len(B):
    if not len(A):
        C.extend(B)
        B = []
        continue
    else:
        a_ = A[0]

    if not len(B):
        C.extend(A)
        A = []
        continue
    else:
        b_ = B[0]

    if a_ > b_:
        C.append(B.popleft())
    else:
        C.append(A.popleft())

print ' '.join(map(str, C))

