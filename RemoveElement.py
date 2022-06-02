"""
Question:

Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The relative order of the elements may be changed.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.
"""
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        # Create pointers
        searcher = 0
        replacer = len(nums) - 1

        # Create the while loop
        while searcher <= replacer:

            # value found
            if nums[searcher] == val:
                # Make a match with replacer

                # If we encounter an area already used
                if nums[searcher] == nums[replacer]:
                    # We update replacer
                    replacer -= 1
                    searcher -= 1
                else:
                    # Swap
                    nums[searcher], nums[replacer] = nums[replacer], nums[searcher]

            searcher += 1

        return searcher

    """
    Answer:

    We need two pointers - one for searching and the other for replacing
    the searcher will move from left the the replacer will move from right, 
    if we encounter a value, 
        we check if the replacer has a slot for us: if not we move the replace backwards by 1 index
        or else we swap the values

    we do this until the replace and the searcher meet

    """