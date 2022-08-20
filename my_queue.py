class Queue:
    def __init__(self):
        self.queue = []

    def insert(self, data):
        self.queue.insert(0, data)

    def peek(self):
        return self.queue[-1]

    def pop(self):
        if len(self.queue):
            self.queue.pop()
        else:
            print("Queue is empty")

    def view(self):
        i = len(self.queue) - 1
        while i >= 0:
            print(self.queue[i])
            i -= 1

    def add_me_front(self, data):
        self.queue.append(data)



obj = Queue()
obj.insert("Mon")
obj.insert("Tue")
obj.insert("Wed")
obj.insert("Thur")
print("\nViewing all the elements")
obj.view()
print("\nRemoving the first element Mon")
obj.pop()
obj.view()
print("\nPeek first element ", obj.peek())
print("\nViewing elements after adding an Mon in the front")
obj.add_me_front("Mon")
obj.view()

