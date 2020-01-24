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

    def insertion_sort(self):
        for i in range(1, self.len):
            ele = self.nums[i]
            j = i - 1
            while j >= 0 and ele < self.nums[j]:
                self.nums[j + 1] = self.nums[j]
                j = j - 1
            self.nums[j + 1] = ele
            plt.bar(self.y_axis, self.nums, color='orange')
            self.cam.snap()

    def partition(self, arr, left, right):
        i = left - 1
        pivot = arr[right]
        for j in range(left, right):
            if arr[j] <= pivot:
                i = i + 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i+1], arr[right] = arr[right], arr[i+1]
        plt.bar(self.y_axis, arr, color='orange')
        self.cam.snap()
        return i + 1

    def quick_sort(self, arr, left, right):
        if left < right:
            pivot = self.partition(arr, left, right)
            self.quick_sort(arr, left, pivot - 1)
            self.quick_sort(arr, pivot + 1, right)

    def merge(self, arr, left, mid, right):
        n1 = mid - left + 1
        n2 = right - mid
        arr_left = [0] * n1
        arr_right = [0] * n2
        for i in range(0, n1):
            arr_left[i] = arr[left + i]

        for j in range(0, n2):
            arr_right[j] = arr[mid + 1 + j]
        i = 0
        j = 0
        k = left

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

    def merge_sort(self, arr, left, right):
        if left < right:
            m = int((left + right) / 2)
            self.merge_sort(arr, left, m)
            self.merge_sort(arr, m + 1, right)
            self.merge(arr, left, m, right)

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

    def selection_sort(self):
        y_axis = np.arange(self.len)
        plt.bar(y_axis, self.nums, color='orange')
        self.cam.snap()
        for i in range(0, self.len - 1, 1):
            min_ele_pos = i
            for j in range(i + 1, self.len, 1):
                if self.nums[j] < self.nums[min_ele_pos]:
                    min_ele_pos = j
            temp = self.nums[i]
            self.nums[i] = self.nums[min_ele_pos]
            self.nums[min_ele_pos] = temp
            plt.bar(y_axis, self.nums, color='orange')
            self.cam.snap()

    def heapify(self, arr, n, i):
        largest = i
        left = 2*i + 1
        right = 2*i + 2
        if left < n and arr[i] < arr[left]:
            largest = left
        if right < n and arr[largest] < arr[right]:
            largest = right
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self.heapify(arr, n, largest)

    def heap_sort(self):
        y_axis = np.arange(self.len)
        plt.bar(y_axis, self.nums, color='orange')
        self.cam.snap()
        n = int(self.len/2)
        for i in range(n - 1, -1, -1):
            self.heapify(self.nums, self.len, i)
        for i in range(self.len-1,  -1, -1):
            self.nums[0], self.nums[i] = self.nums[i], self.nums[0]
            plt.bar(y_axis, self.nums, color='orange')
            self.cam.snap()
            self.heapify(self.nums, i, 0)


def main():
    parser = argparse.ArgumentParser(description='Train Dependency Parsing Model')
    parser.add_argument('--len', type=int, default=5, help='Array size')
    parser.add_argument('--algo', type=str, help='Sorting Algorithm')
    args = parser.parse_args()
    algo_choices = ['bubble_sort', 'insertion_sort', 'selection_sort', 'heap_sort', 'merge_sort', 'quick_sort']

    len = args.len
    elapsed_time = 0
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
        print("Time : ", elapsed_time)

    elif alg == "merge":
        start_time = time.time()
        obj1.merge_sort(nums, 0, len - 1)
        elapsed_time = time.time() - start_time
        print("Time : ", elapsed_time)

    elif alg == "quick":
        start_time = time.time()
        obj1.quick_sort(nums, 0, len - 1)
        elapsed_time = time.time() - start_time
        print("Time : ", elapsed_time)

    elif alg == "insertion":
        start_time = time.time()
        obj1.insertion_sort()
        elapsed_time = time.time() - start_time
        print("Time : ", elapsed_time)

    elif alg == "selection":
        start_time = time.time()
        obj1.selection_sort()
        elapsed_time = time.time() - start_time
        print("Time : ", elapsed_time)

    elif alg == "heap":
        start_time = time.time()
        obj1.heap_sort()
        elapsed_time = time.time() - start_time
        print("Time : ", elapsed_time)

    elif alg == "all":

        for i in range(0, 4):
            start_time = time.time()
            getattr(obj1, algo_choices[i])()
            elapsed_time = time.time() - start_time
            print(algo_choices[i] + " Time : ", elapsed_time)

        for i in range(4, 6):
            start_time = time.time()
            getattr(obj1, algo_choices[i])(nums, 0, len - 1)
            elapsed_time = time.time() - start_time
            print(algo_choices[i] + " Time : ", elapsed_time)

    animation = cam.animate(interval=800, blit=True, repeat=False, repeat_delay=1000)
    animation.save(alg + '_sort_animation.gif', writer='imagemagick')


if __name__ == '__main__':
    main()
