class Solution(object):
    def minPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        result = []
        i=0
        j=len(nums)-1
        n=len(nums)//2
        sums = 0
        while (i<n and j >= n):
            sums = nums[i] + nums[j]
            result.append(sums)
            i +=1
            j -=1
        return max(result)