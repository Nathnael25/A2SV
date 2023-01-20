class MyCircularDeque(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.deque = [None] * k
        self.front = self.rear = -1
        self.size = k

    def insertFront(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        if self.front == -1:
            self.front = 0
            self.rear = 0
        elif self.front == 0:
            self.front = self.size - 1
        else:
            self.front -= 1
        self.deque[self.front] = value
        return True

    def insertLast(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        if self.front == -1:
            self.front = 0
            self.rear = 0
        elif self.rear == self.size - 1:
            self.rear = 0
        else:
            self.rear += 1
        self.deque[self.rear] = value
        return True

    def deleteFront(self):
        """
        :rtype: bool
        """
        if self.isEmpty():
            return False
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        elif self.front == self.size - 1:
            self.front = 0
        else:
            self.front += 1
        return True

    def deleteLast(self):
        """
        :rtype: bool
        """
        if self.isEmpty():
            return False
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        elif self.rear == 0:
            self.rear = self.size - 1
        else:
            self.rear -= 1
        return True

    def getFront(self):
        """
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.deque[self.front]

    def getRear(self):
        """
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.deque[self.rear]

    def isEmpty(self):
        """
        :rtype: bool
        """
        return self.front == -1

    def isFull(self):
        """
        :rtype: bool
        """
        return (self.front == 0 and self.rear == self.size-1) or (self.front == self.rear+1)
