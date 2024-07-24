from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        stash = set(nums)
        res = 0

        for num in nums:
            if (num - 1) not in stash:
                length = 1
                while (num + length) in stash:
                    length += 1
                res = max(length, res)
        return res