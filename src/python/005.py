
"""
date: 2019-02-22 18:20:30
排序代码集合
"""


def merge_sort(a: list):
    """
    归并排序
    算法思路：
    时间复杂度：O(n^2)，最好：O(n)，最坏：O(n^2)
    空间复杂度：O(1)
    """
    cnt = len(a)
    if cnt < 2:
        return a
    mid = cnt // 2
    print(mid)
    left = a[0: mid]
    right = a[mid:cnt]
    return merge(merge_sort(left), merge_sort(right))


def merge(left: list, right: list):
    result = []
    left_cnt = len(left)
    right_cnt = len(right)
    left_index = 0
    right_index = 0
    for i in range(left_cnt+right_cnt):
        if left_index >= left_cnt:
            result[i] = right[right_index]
            right_index += 1
        elif right_index >= right_cnt:
            result[i] = left[left_index]
            left_index += 1
        elif left[left_index] > right[right_index]:
            print(right_index)
            result[i] = right[right_index]
            right_index += 1
        else:
            result[i] = left[left_index]
            left_index += 1
    return result


if __name__ == '__main__':
    a = [2, 1, 4, 6, 3, 45, 76, 47, 34, 5, 23]
    merge_sort(a)
    print(a)
