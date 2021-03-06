class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.newQueue = []
        

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.newQueue.append(x)
        

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        return self.newQueue.pop(0)
        

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        return self.newQueue[0]
        

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        if len(self.newQueue) >= 1:
            
            return False
        
        else:
             return True


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()