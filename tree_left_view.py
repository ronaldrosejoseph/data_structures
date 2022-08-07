class Tree:
    def __init__(self, data):
        self.left = self.right = None
        self.data = data

    def left_view(self, left=[]):
        left.append(self.data)
        if self.left:
            self.left.left_view(left)
        elif self.right:
            self.right.left_view(left)

        return left


'''

        10
        /\
       6  16
      /\  /\
     4  7 15 19
    \  /\ /\ /\
    5 3 8 13 17 18 20

'''
obj = Tree(10)
obj.left = Tree(6)
obj.left.left = Tree(4)
obj.left.right = Tree(7)
obj.left.left.right = Tree(5)
obj.left.right.left = Tree(3)
obj.left.right.right = Tree(8)
obj.right = Tree(16)
obj.right.left = Tree(15)
obj.right.left.left = Tree(13)
obj.right.left.right = Tree(17)
obj.right.right = Tree(19)
obj.right.right.left = Tree(18)
obj.right.right.right = Tree(20)

print(obj.left_view())
