"""
Question:
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

"""
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        nums1Copy = nums1[:m]

        p1 = 0
        p2 = 0
        p = 0

        while p < m + n:
            # Comparing which one is lesser
            if p2 >= n or (p1 < m and nums1Copy[p1] <= nums2[p2]):

                # Writing into main num1
                nums1[p] = nums1Copy[p1]
                p1 += 1
            else:
                nums1[p] = nums2[p2]
                p2 += 1
            p += 1

            # TIme complexity O(n)
            # Space complexity O(n)

        """
        Pseudocode:

        We make copies of the array for nums1
        we create pointer for each array 

        two read pointers for each of copy of num1 and that of num2

        we loop through original num1 once, and use the pointer of numCopy to compare its value with the nums2 value with its pointer
        We write the lesser one in the main num and move the pointer whose value was updated by 1

        and we also update the pointer for main num
        """

        # BRUTE FORCE
        # the brute force approach is to append nums2 into main nums1 and sort. However that will be O(logn)