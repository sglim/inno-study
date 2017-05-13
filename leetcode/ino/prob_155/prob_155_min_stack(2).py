class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        self.min_value = 0


    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if len(self.data) <= 0:
            self.min_value = x
            self.data.append(0)
        else:
            self.data.append(x - self.min_value)
            if x < self.min_value:
                self.min_value = x

    def pop(self):
        """
        :rtype: void
        """
        top_value = self.data.pop()

        if top_value < 0:
            self.min_value = self.min_value - top_value


    def top(self):
        """
        :rtype: int
        """
        last_idx = len(self.data) - 1
        top_value = self.data[last_idx]

        if top_value < 0:
            return self.min_value
        else:
            return top_value + self.min_value


    def getMin(self):
        """
        :rtype: int
        """
        return self.min_value



