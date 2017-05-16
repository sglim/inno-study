class MyStack(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = []
        self.queue.append([])
        self.queue.append([])
        self.activated = 0
        self.inactivated = 1

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.queue[self.activated].append(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        self.temp = 0
        while True:
            self.temp = self.queue[self.activated].pop(0)
            if len(self.queue[self.activated]) == 0:
                break
            self.queue[self.inactivated].append(self.temp)

        self.activated = self.inactivated
        self.inactivated = (self.inactivated + 1) % 2
        return self.temp

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        self.temp = 0
        while len(self.queue[self.activated]) != 0:
            self.temp = self.queue[self.activated].pop(0)
            self.queue[self.inactivated].append(self.temp)

        self.activated = self.inactivated
        self.inactivated = (self.inactivated + 1) % 2
        return self.temp

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return len(self.queue[self.activated]) == 0


# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(2)
obj.push(4)
print(obj.top())
obj.pop()
print(obj.top())
