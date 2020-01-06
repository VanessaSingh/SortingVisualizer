from matplotlib import pyplot as plt
from celluloid import Camera
import numpy as np
import sys
import time
import argparse

sys.setrecursionlimit(1500)


class Sort:
    def __init__(self, nums, len, cam):
        self.nums = nums
        self.len = len
        self.cam = cam
        self.ans = self.nums
        self.y_axis = np.arange(self.len)
        plt.bar(self.y_axis, self.nums, color='orange')
        self.cam.snap()

    def partition(self, arr, l, r):
        i = l - 1
        pivot = arr[r]
        for j in range(l, r):
            if arr[j] <= pivot:
                i = i + 1
                t = arr[i]
                arr[i] = arr[j]
                arr[j] = t
        t = arr[i + 1]
        arr[i + 1] = arr[r]
        arr[r] = t
        plt.bar(self.y_axis, arr, color='orange')
        self.cam.snap()
        return i + 1

    def quick_sort(self, arr, l, r):
        if l < r:
            p = self.partition(arr, l, r)
            self.quick_sort(arr, l, p - 1)
            self.quick_sort(arr, p + 1, r)

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

    def merge_sort(self, arr, l, r):
        if l < r:
            m = int((l + r) / 2)
            self.merge_sort(arr, l, m)
            self.merge_sort(arr, m + 1, r)
            self.merge(arr, l, m, r)

    def bubble_sort(self):
        y_axis = np.arange(self.len)
        plt.bar(y_axis, self.nums, color='orange')
        self.cam.snap()
        for i in range(0, self.len - 1, 1):
            for j in range(0, self.len - i - 1, 1):
                if self.nums[j] > self.nums[j + 1]:
                    temp = self.nums[j]
                    self.nums[j] = self.nums[j + 1]
                    self.nums[j + 1] = temp
                    plt.bar(y_axis, self.nums, color='orange')
                    self.cam.snap()


def main():
    parser = argparse.ArgumentParser(description='Train Dependency Parsing Model')
    parser.add_argument('--len', type=int, default=5, help='Array size')
    parser.add_argument('--algo', type=str, help='Sorting Algorithm')
    args = parser.parse_args()
    len = args.len
    alg = args.algo
    nums = []
    for i in range(len, 0, -1):
        nums.append(i)
    fig = plt.figure()
    cam = Camera(fig)
    obj1 = Sort(nums, len, cam)
    if alg == "bubble":
        start_time = time.time()
        obj1.bubble_sort()
        elapsed_time = time.time() - start_time

    elif alg == "merge":
        start_time = time.time()
        obj1.merge_sort(nums, 0, len - 1)
        elapsed_time = time.time() - start_time

    elif alg == "quick":
        start_time = time.time()
        obj1.quick_sort(nums, 0, len - 1)
        elapsed_time = time.time() - start_time
    print("Time : ", elapsed_time)
    animation = cam.animate(interval=800, blit=True, repeat=False, repeat_delay=1000)
    animation.save(alg + '_sort_animation.gif', writer='imagemagick')


if __name__ == '__main__':
    main()
