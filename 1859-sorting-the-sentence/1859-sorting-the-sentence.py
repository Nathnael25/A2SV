class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        shfl = s.split(" ")
        final = ""
        for i in range (len(shfl)):
            k=i
            
            for j in range(i+1,len(shfl)):
                if shfl[j][-1] < shfl[k][-1]:
                    k=j
                    
            if k!=i:
                shfl[i], shfl[k] = shfl[k], shfl[i]
            final += shfl[i][:-1] + ' '
        
        return (final[:-1]) 