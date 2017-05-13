class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        self.min_stack = []
        self.min_value = 0


    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if len(self.data) <= 0 or x < self.min_value:
            self.min_value = x

        self.data.append(x)
        self.min_stack.append(self.min_value)


    def pop(self):
        """
        :rtype: void
        """
        self.min_stack.pop()
        last_idx = len(self.min_stack) - 1
        if last_idx >= 0:
            self.min_value = self.min_stack[last_idx]
        return self.data.pop()


    def top(self):
        """
        :rtype: int
        """
        last_idx = len(self.data) - 1
        return self.data[last_idx]


    def getMin(self):
        """
        :rtype: int
        """
        last_idx = len(self.min_stack) - 1
        return self.min_stack[last_idx]



