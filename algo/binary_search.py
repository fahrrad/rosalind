__author__ = 'CoesseWa'


def parse_file(filename):
    with open(filename, 'r') as f:
        sorted_array_c = int(f.readline())
        integers_c = int(f.readline())
        sorted_array = [int(x) for x in f.readline().strip().split(' ')]
        integers = [int(x) for x in f.readline().strip().split(' ')]

        if (len(sorted_array) != int(sorted_array_c)) or (len(integers) != int(integers_c)):
            raise Exception('something went wrong while parsing the file. ')

    return sorted_array, integers


def binary_search(sorted_array, element, i_from, i_to):
    """tries to find the element in sorted_array, and returns 1-based index if it finds is, and -1 if it don't"""

    if i_from == i_to:
        if element == sorted_array[i_from]:
            return i_from + 1
        else:
            return -1

    # check middle element in interval
    else:
        i_2 = (i_to - i_from) / 2
        if sorted_array[i_from + i_2] == element:
            return i_from + i_2 + 1
        elif sorted_array[i_from + i_2] > element:
            return binary_search(sorted_array, element, i_from, i_from + i_2)
        else:
            return binary_search(sorted_array, element, i_to - i_2, i_to)


if __name__ == '__main__':
    (sorted_array, integers) = parse_file('rosalind_bins.txt')

    print len(sorted_array), " sorted array"
    print len(integers), " integers array"

    print ' '.join([str(binary_search(sorted_array, x, 0, len(sorted_array) - 1)) for x in integers])
