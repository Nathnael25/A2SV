class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        import collections 
        counter = collections.Counter(list(s))
        for i in range(len(s)):
            if counter.get(s[i])==1:
                return i
        return -1