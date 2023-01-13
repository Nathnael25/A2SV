class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        mp = {}
        an = []
        for i in nums:
            mp[i] = mp.get(i,0)+1
        
        
        l = []
        heapq.heapify(l)
       
    
        
        for i in mp:
            heapq.heappush(l,[-mp[i],i])
        
        
        
        while k>0:
            z = heapq.heappop(l)
            an.append(z[1])
            k-=1
        return an