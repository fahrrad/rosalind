__author__ = 'CoesseWa'
"""Degree Array. Works only in python 2.7!"""
from collections import defaultdict

def parse_edgle_list(filename):
    edge_list = []
    degrees = defaultdict(int)
    with open('../data/' + filename, 'rt') as inf:
        v, e = map(int, inf.readline().strip().split(' '))
        vertices = range(1, 1 + v)
        adj_list = {x: [] for x in vertices}
        for line in inf.readlines():
            edge = map(int, line.strip().split(' '))
            edge_list.append(edge)
            a,b = edge

            adj_list[a].append(b)
            adj_list[b].append(a)

            degrees[a] += 1
            degrees[b] += 1

    return vertices, edge_list, degrees, adj_list


if __name__ == '__main__':
    V, E, D, A = parse_edgle_list('rosalind_ddeg.txt')

    print 'degrees : '
    print ' '.join(map(lambda x: str(D[x]), V))

    print 'sum of neigbour degrees: '
    for n_neigbours in (A[x] for x in V):
        s_degrees = sum(map(lambda x: D[x], n_neigbours))
        print s_degrees,

