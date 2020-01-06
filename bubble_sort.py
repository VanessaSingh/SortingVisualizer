from matplotlib import pyplot as plt
from celluloid import Camera
import numpy as np
import sys

sys.setrecursionlimit(1500)


class Sort:
    def __init__(self, nums, len, cam):
        print("In init of Sort")
        self.nums = nums
        self.len = len
        self.cam = cam
        self.ans = self.nums
        self.y_axis = np.arange(self.len)
        plt.bar(self.y_axis, self.nums, color='orange')

    def merge(self, arr, l, m, r):
        n1 = m - l + 1
        n2 = r - m
        arr_left = [0] * n1
        arr_right = [0] * n2
        for i in range(0, n1):
            arr_left[i] = arr[l + i]

        for j in range(0, n2):
            arr_right[j] = arr[m + 1 + j]
        i = 0
        j = 0
        k = l

        while i < n1 and j < n2:
            if arr_left[i] <= arr_right[j]:
                arr[k] = arr_left[i]
                i = i + 1
            else:
                arr[k] = arr_right[j]
                j = j + 1
            k = k + 1
        while i < n1:
            arr[k] = arr_left[i]
            i = i + 1
            k = k + 1
        while j < n2:
            arr[k] = arr_right[j]
            j = j + 1
            k = k + 1
        plt.bar(self.y_axis, arr, color='orange')
        self.cam.snap()
        print(arr)

    def merge_sort(self, arr, l, r):
        if l < r:
            m = int((l + r) / 2)
            self.merge_sort(arr, l, m)
            self.merge_sort(arr, m + 1, r)
            self.merge(arr, l, m, r)

    def bubble_sort(self):
        print("In bubble sort")
        y_axis = np.arange(self.len)
        plt.bar(y_axis, self.nums, color='blue')
        # plt.plot(self.nums)
        self.cam.snap()
        for i in range(0, self.len - 1, 1):
            for j in range(0, self.len - i - 1, 1):
                if self.nums[j] > self.nums[j + 1]:
                    temp = self.nums[j]
                    self.nums[j] = self.nums[j + 1]
                    self.nums[j + 1] = temp
                    # plt.plot(self.nums)
                    plt.bar(y_axis, self.nums, color='blue')
                    self.cam.snap()
        animation = self.cam.animate(interval=500, blit=True, repeat=False, repeat_delay=1000)
        animation.save('bubble_sort_animation.gif', writer='imagemagick')
        print(self.nums)


def main():
    print("Enter length: ")
    len = int(input())
    nums = []
    for i in range(len, 0, -1):
        nums.append(i)
    fig = plt.figure()
    cam = Camera(fig)
    obj1 = Sort(nums, len, cam)
    # obj1.bubble_sort()
    print(nums)
    # y_axis = np.arange(len)
    # plt.bar(y_axis, nums, color='orange')
    cam.snap()
    obj1.merge_sort(nums, 0, len - 1)
    print(nums)
    animation = cam.animate(interval=800, blit=True, repeat=False, repeat_delay=1000)
    animation.save('merge_sort_animation.gif', writer='imagemagick')


if __name__ == '__main__':
    main()
