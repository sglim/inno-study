# stack implementation practice


class Stack(object):

    def __init__(self):
        self.data = []

    def push(self, value):
        self.data.append(value)

    def pop(self):
        if self.is_empty():
            print("the stack is empty")
            return None
        else:
            return self.data.pop()

    @property
    def size(self):
        return len(self.data)

    def is_empty(self):
        return self.size <= 0

    def peek(self):
        if self.is_empty():
            print('the stack is empty')
            return None
        else:
            return self.data[self.size-1]

    def print_stack(self):
        if self.is_empty():
            print('the stack is empty')
        else:
            print(self.data)


stk = Stack()
stk.pop()

# implementation test
# uncomment each line to test

test_stack = Stack()

print("the stack is empty now? : ", test_stack.is_empty())
print("check size : ", test_stack.size)

print("push 7 now")
test_stack.push(7)
print ("")

print("the stack is empty now? : ", test_stack.is_empty())
print("peek value : ", test_stack.peek())
print("check size : ", test_stack.size)
test_stack.print_stack()
print ("")

print("push 8,4,12,-7,0,55")
for i in [8, 4, 12, -7, 0, 55]:
    test_stack.push(i)
print("check peek value : ", test_stack.peek())
print("check size : ", test_stack.size)
test_stack.print_stack()
print ("")

print("pop : ", test_stack.pop())
print("check peek value : ", test_stack.peek())
print("check size : ", test_stack.size)
test_stack.print_stack()
print ("")

print("pop : ", test_stack.pop())
print("pop : ", test_stack.pop())
print("pop : ", test_stack.pop())
print("check peek value : ", test_stack.peek())
print("check size : ", test_stack.size)
test_stack.print_stack()
print ("")

print("pop : ", test_stack.pop())
print("pop : ", test_stack.pop())
print("pop : ", test_stack.pop())
print("check size : ", test_stack.size)
test_stack.print_stack()
print ("")

print("pop : ", test_stack.pop())
print("check size : ", test_stack.size)
test_stack.print_stack()
print ("")

print("push 27,1,-8")
for i in [27, 1, -8]:
    test_stack.push(i)
print("check peek value : ", test_stack.peek())
print("check size : ", test_stack.size)
test_stack.print_stack()
print ("")
