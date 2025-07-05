#!/usr/bin/python3

from typing import List


class Solution:
    def findLucky(self, arr: List[int]) -> int:
        # count the frequencies of each number in array
        freq = {}
        for num in arr:
            freq[num] = freq.get(num, 0) + 1

        # compile a list of lucky numbers
        lucky_nums = [k for k, v in freq.items() if k == v]

        # return the largest lucky number
        return max(lucky_nums, default=-1)


if __name__ == "__main__":
    solution = Solution()
    print(solution.findLucky([1,2,3,3,3]))
