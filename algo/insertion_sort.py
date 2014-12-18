__author__ = 'CoesseWa'

swaps = 0


def insert_sort(A):
    global swaps
    for i in range(1, len(A)):
        k = i
        while k > 0 and A[k] < A[k-1]:
            x = A[k]
            A[k] = A[k-1]
            A[k-1] = x
            swaps += 1

            k -= 1
    return A

c = 0
A = []
with open('rosalind_insert_sort', 'rt') as f:
    c = f.readline().strip()
    A = map(int, f.readline().strip().split(' '))


print ' '.join(map(str, insert_sort(A)))
print swaps
