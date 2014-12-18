from collections import defaultdict

__author__ = 'CoesseWa'

arrays = []
k = n = 0

with open('rosalind_maj.txt', 'rt') as f:
    k, n = map(int, f.readline().strip().split(' '))
    for array in f.readlines():
        arrays.append(map(int, array.strip().split(' ')))


def maj_element(array):
    counts = defaultdict(int)
    max_c = 0

    for elem in array:
        if max_c == counts[elem]:
            max_c += 1

        counts[elem] += 1

        if max_c > n / 2:
            return elem

    return -1

print ' '.join([str(x) for x in map(maj_element, arrays)])