class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        stash = set()
        for num in nums:
            if num in stash:
                return True
            stash.add(num)
        return False