class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        ans = 0
        n = len(arr)
        
        for i in range(n):
            for j in range (i+1, n+1):
                if (j-i)%2:
                    ans+= sum(arr[i:j])
        return ans