class MyQueue(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = [[], []]
        self.use = 0
        self.notuse = 1
        self.peek_val = 0

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        if self.empty():
            self.peek_val = x
        self.stack[self.use].append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        temp = 0
        move = 0

        while True:
            temp = self.stack[self.use].pop()
            if self.empty():
                not_use_last_idx = len(self.stack[self.notuse]) - 1
                if not_use_last_idx >= 0:
                    self.peek_val = self.stack[self.notuse][not_use_last_idx]
                break
            self.stack[self.notuse].append(temp)

        while len(self.stack[self.notuse]) != 0:
            move = self.stack[self.notuse].pop()
            self.stack[self.use].append(move)
        return temp

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        return self.peek_val

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return len(self.stack[self.use]) == 0


# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(1)
print(obj.pop())
print(obj.empty())

# obj.push(2)
# obj.push(3)
# print(obj.peek())
# print(obj.pop())
# obj.push(4)
# print(obj.peek())
