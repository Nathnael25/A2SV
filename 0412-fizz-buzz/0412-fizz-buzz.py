class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        list = []
        for i in range (1, n+1):
            if ((i%3==0 and i%5==0)):
                list.append("FizzBuzz")
            elif(i%3 == 0):
                list.append("Fizz")
            elif(i%5 == 0):
                list.append("Buzz")
            else:
                i = str (i)
                list.append(i)
        return list      
            
        