class Solution(object):
    def kthLargestNumber(self, nums, k):
        """
        :type nums: List[str]
        :type k: int
        :rtype: str
        """
        change = []
        for i in range (0,len(nums)):
            change.append(int(nums[i]))
            change = sorted(change)
        return str(change[len(change)-k])
            