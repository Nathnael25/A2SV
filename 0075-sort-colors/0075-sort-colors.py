class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            k = i
            for j in range(i+1,len(nums)):
                if nums[j]<nums[k]:
                    k=j
            if k!=i:
                nums[i],nums[k] = nums[k],nums[i]
        
        
        