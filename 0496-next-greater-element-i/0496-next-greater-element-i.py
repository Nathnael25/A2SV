class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        stack = []
        next_greater = {}
        ans = []
        for num in nums2:
            while len(stack) > 0 and stack[-1] < num:
                next_greater[stack.pop()] = num
            stack.append(num)
        for num in nums1:
            ans.append(next_greater.get(num, -1))
        return ans
            
        
        