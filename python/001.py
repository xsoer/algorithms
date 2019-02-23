"""
date: 2019-02-22 18:20:30
排序代码集合
"""

a = [2, 1, 4, 6, 3, 45, 76, 47, 34, 5, 23]


def pop_sort():
    """
    冒泡排序
    算法思路：需要有两个游标，第一个从大范围从头遍历；第二个从第一个游标的位置+1处开始往后遍历；
    第一个游标的值和第二个游标的值进行比较，如果第一个比第二个大，就调整位置
    时间复杂度：O(n^2)，最好：，最坏：
    空间复杂度：O(1)
    """
    cnt = len(a)
    for i in range(cnt):
        for j in range(cnt)[i:]:
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]
    print(a)


def insert_sort():
    """
    插入排序
    算法思路：
    时间复杂度：
    空间复杂度：
    """
    pass


def quick_sort():
    """
    快速排序
    """
    pass


def dui_sort():
    """
    堆排序
    """
    pass


if __name__ == '__main__':
    pop_sort()
