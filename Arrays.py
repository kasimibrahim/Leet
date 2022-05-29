class Arrays:

    def __init__(self):
        self.array = []

    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # ALGORITHM
        """We keep track of the ones with prev, if we encounter a zero, we check if this was the first occurance with
         the first if, thus we have not declared a value for nxt so it is zero, if we already have then the prev must
          be bigger before we transfer that value to nxt and reset prev"""
        prev = 0
        nxt = 0
        for bit in nums:
            if bit == 1:
                prev += 1
            else:
                if nxt == 0:
                    nxt = prev
                if prev > nxt:
                    nxt = prev
                prev = 0
        if prev > nxt:
            return prev
        return nxt

    # Given an array nums of integers, return how many of them contain an even number of digits.
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        even = 0
        for n in nums:
            if len(str(n)) % 2 == 0:
                even += 1
        return even


    def transpose(self, matrix):
        for row in matrix:
            print(row[1])




if __name__ == "__main__":

    example = Arrays()

    matrix = [
                [1,2,3],
                [4,5,6],
                [7,8,9]
            ]

    example.transpose()


