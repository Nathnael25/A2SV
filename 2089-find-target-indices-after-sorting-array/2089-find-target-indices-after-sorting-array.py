class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        sortedNums = sorted(nums)
        index=[]
        
        for i in range(len(sortedNums)):
            if target == sortedNums[i]:
                index.append(i)
        return index
        