class Solution(object):
    def checkArithmeticSubarrays(self, nums, l, r):
        """
        :type nums: List[int]
        :type l: List[int]
        :type r: List[int]
        :rtype: List[bool]
        """
        dic = {}
        ans = []
        
        for i in range(len(l)):
            dic[i] = nums[l[i]:r[i]+1]
        for num in dic:
            j = 0
            dic[num].sort()
            for i in range(2,len(dic[num])):
                if dic[num][i]-dic[num][i-1]!=dic[num][1]-dic[num][0]:
                    ans.append(False)
                    break
                j+=1
            if j==len(dic[num])-2:
                ans.append(True)
        return ans