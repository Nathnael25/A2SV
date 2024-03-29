class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        heap=[]
        for x,y in points:
            heapq.heappush(heap,((math.sqrt(x**2+y**2)),[x,y]))
        output=[]
        K=1
        while heap and K<=k:
            h = heapq.heappop(heap)
            output.append (h[1])
            K+=1
        return output