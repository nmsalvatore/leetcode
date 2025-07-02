from typing import List

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        harmonious_length = 0
        for count in counts:
            if count + 1 in counts:
                # Since a harmonious subsequence can only have a
                # difference of 1 between the max and min values, the
                # sum of the two counts are equal to the length of
                # the harmonious subsequence. The maximum sum found is
                # the longest harmonious subsequence.
                harmonious_length = max(harmonious_length, counts[count] + counts[count + 1])

        return harmonious_length
