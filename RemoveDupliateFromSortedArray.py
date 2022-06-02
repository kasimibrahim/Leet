class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        # Set up a pointers
        replacer = 0

        # We move from left to right, if we encounter a different number, then we swap

        for i in range(len(nums)):

            if nums[replacer] != nums[i]:
                nums[replacer + 1] = nums[i]
                replacer += 1
        return replacer + 1

        """
        p
        i

        [0, 0, 1, 1, 2 ,3, 4]


         p
            i                #Same so we wont trnafer value

        [0, 0, 1, 1, 2 ,3, 4]



        p
               i                #Different so we transfer value with the one immediately in front of p, and move p by 1

        [0, 0, 1, 1, 2 ,3, 4]


            p
               i                #Different so we transfer value with the one immediately in front of p

        [0, 1, 1, 1, 2 ,3, 4]


            p
                  i           

        [0, 1, 1, 1, 2 ,3, 4]


               p
                     i           

        [0, 1, 2, 1, 2 ,3, 4]


                  p
                        i           

        [0, 1, 2, 3, 2 ,3, 4]


                     p
                           i           

        [0, 1, 2, 3, 4 ,3, 4]


        Then we return array up to where p is, thus [0,1,2,3,4]
        """