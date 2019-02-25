
"""
date: 2019-02-25 10:01
排序代码集合
"""


def quick_sort(array, l, r):
    if l < r:
        q = partition(array, l, r)
        quick_sort(array, l, q)
        quick_sort(array, q + 1, r)


def partition(array, l, r):
    i = l - 1
    for j in range(l, r):
        if array[j] <= array[r]:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i+1], array[r] = array[r], array[i+1]
    return i


if __name__ == '__main__':
    a = [2, 1, 4, 6, 3, 45, 76, 47, 34, 5, 23]
    quick_sort(a, 0, len(a) - 1)
    print(a)
