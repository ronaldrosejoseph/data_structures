class Tree:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def print_tree(self, preorder, inorder, postorder):
        preorder.append(self.data)
        if self.left:
            self.left.print_tree(preorder, inorder, postorder)
        inorder.append(self.data)
        if self.right:
            self.right.print_tree(preorder, inorder, postorder)
        postorder.append(self.data)
        return preorder, inorder, postorder



'''

preorder 10-6-4-2-5-7-3-8-16-15-13-17-19-18-20-
inorder 2-4-5-6-3-7-8-10-13-15-17-16-18-19-20-
postorder 2-5-4-3-8-7-6-13-17-15-18-20-19-16-10-

        10
        /\
       6  16
      /\  /\
     4  7 15 19
   /\  /\ /\ /\
  2 5 3 8 13 17 18 20
  
'''
obj = Tree(10)
obj.left = Tree(6)
obj.left.left = Tree(4)
obj.left.right = Tree(7)
obj.left.left.left = Tree(2)
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

pre, inn, post = obj.print_tree([], [], [])

print(pre)
print(inn)
print(post)

