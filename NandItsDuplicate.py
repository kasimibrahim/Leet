class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        multiple_of_2 = False
        for i in range(len(arr)):
            for j in range(len(arr)):
                if arr[i] == arr[j] * 2 and i != j:  # this i != j is checking for when the number checks itself, for example 0 is a multiole of 2 of itself
                    multiple_of_2 = True
                    break

        return multiple_of_2
