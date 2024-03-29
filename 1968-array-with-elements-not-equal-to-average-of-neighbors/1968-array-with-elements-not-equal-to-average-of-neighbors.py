class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums=sorted(nums)
        result = []
        
        l, r = 0, len(nums)-1
        while len(result)!= len(nums):
            result.append(nums[l])
            l+=1
            
            if l<=r:
                result.append(nums[r])
                r-=1
        return result 
                
            