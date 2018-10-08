class Stack:
    def __init__(self):
        self.stack = []

    def append(self, data):
        self.stack.append(data)

    def peek(self):
        return self.stack[-1]

    def pop(self):
        if len(self.stack):
            self.stack.pop()
        else:
            print("Stack is empty")

    def view(self):
        i = len(self.stack) - 1
        while i >= 0:
            print(self.stack[i])
            i -= 1


obj = Stack()
obj.append("Mon")
obj.append("Tue")
obj.append("Wed")
obj.append("Thur")
print("\nViewing all the elements")
obj.view()
print("\nRemoving top element Thur")
obj.pop()
obj.view()
print("\nPeek top element ", obj.peek())


