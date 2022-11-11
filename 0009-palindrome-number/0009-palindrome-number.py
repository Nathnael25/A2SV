class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        reverse = 0
        y = x
        
        if x < 0 :
            return False 
        elif x >= 0:
            while x != 0:
                digit = x % 10 
                reverse = reverse*10 + digit 
                x = x // 10
                
            if int (reverse) == y :
                return True 
        else:
            return False 