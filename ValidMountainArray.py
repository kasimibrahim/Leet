"""
Given an array of integers arr, return true if and only if it is a valid mountain array.

Recall that arr is a mountain array if and only if:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

Input: arr = [2,1]
Output: false

Input: arr = [3,5,5]
Output: false

Input: arr = [0,3,2,1]
Output: true

"""


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:

        step = 0
        distance = len(arr)

        # climbing up
        # this means if the conditions are true for all distance, then it is not a valid mountain
        while step + 1 < distance and arr[step] < arr[step + 1]:
            step += 1

        # after checking for climbing, we check if we did not move up at all of covered all distance, if true then it is not a mountain
        if step == 0 or step == distance - 1:
            return False

        # after checking for all climbing, we descend to see whether we will cover all the distance
        while step + 1 < distance and arr[step] > arr[step + 1]:
            step += 1

        # If there was no flat surface, then we are supposed to reach destination
        return step == distance - 1
