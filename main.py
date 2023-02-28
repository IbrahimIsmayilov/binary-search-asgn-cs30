nums = [10, 30, 40, 45, 70, 80, 85, 90, 100]
words = ["at", "ball", "cat", "dog", "eye", "fish", "good"]
unsorted = [30, 20, 70, 40, 50, 100, 90]

import math

def binarySearch(anArray, item):
    li = 0
    ui = len(anArray) - 1

    while li <= ui :
        mi = math.floor((li + ui) / 2)
        if anArray[mi] == item:
            return mi
        elif item < mi:
            ui = mi - 1
        else:
            li = mi + 1

    return -1
        


print(binarySearch(nums, 100))
print(binarySearch(nums, 75))
print(binarySearch(words, "fish"))
print(binarySearch(words, "at"))
print(binarySearch(unsorted, 70))