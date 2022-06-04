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

        """
        We want consistency in the gradient so we calculate the gradient for the positive,
        and then the gradient for the negitve.
        these values must be consistent until we are done loop


        so
        we start at x = 1 where x is an index

        then we say
        gradient = arr[x] - arr[x-1] / x - 1
        this is our first gradient, meaning that subsequent gradients should not differ from this one

        thus

        if arr[x_2] - arr[x_1] / x_2 - x_1 != gradient:
              then we return false

        """
        starting_gradient = False
        pos_gradient = 0

        lasting_gradient = False
        neg_gradient = 0

        # looping through
        for step in range(1, len(arr)):

            # for posituve
            if arr[step] > arr[step - 1]:
                if starting_gradient == False:
                    pos_gradient = arr[step] - arr[step - 1]  # Indices increase by 1 always so denominator is not need
                    starting_gradient = True
                    continue
                if arr[step] - arr[step - 1] != pos_gradient:
                    return False

            # for negative
            elif arr[step] < arr[step - 1]:

                # We cannot descend when we have not ascended
                if starting_gradient == False:
                    return False

                if lasting_gradient == False:
                    neg_gradient = arr[step] - arr[step - 1]
                    lasting_gradient = True
                if arr[step] - arr[step - 1] != neg_gradient:
                    return False

            # flat surface a=cannot make a mountain
            else:
                return False

            if neg_gradient < 0 and pos_gradient > 0:
                if abs(neg_gradient) == pos_gradient:
                    return True
                return True
            return False
