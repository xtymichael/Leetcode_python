class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack1 = [] #input
        self.stack2 = [] #output
        

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.stack1.append(x)
        #pushing x to the end of list(queue)

    def pop(self):
        """
        :rtype: nothing
        """
        self.peek()
        self.stack2.pop()

        

    def peek(self):
        """
        :rtype: int
        """
        if not self.stack2:
            while (self.stack1):
                stack2.append(stack1.pop())
        return stack2.pop()

        

    def empty(self):
        """
        :rtype: bool
        """
        return (not self.stack1 and not self.stack2)