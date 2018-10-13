class Tree:
    def __init__(self, data=None):
        self.left = None
        self.right = None
        self.data = data

    def print_tree(self, traversal_type):
        if traversal_type == 'preorder':
            return self.preorder_traversal(self, "")
        elif traversal_type == 'inorder':
            return self.inorder_traversal(self, "")
        elif traversal_type == 'postorder':
            return self.postorder_traversal(self, "")
        else:
            return "you are an idiot"

    def preorder_traversal(self, start, traversal):
        # root -> left -> right
        if start:
            traversal += str(start.data) + '-'
            traversal = self.preorder_traversal(start.left, traversal)
            traversal = self.preorder_traversal(start.right, traversal)
        return traversal

    def inorder_traversal(self, start, traversal):
        # left -> root -> right
        if start:
            traversal = self.inorder_traversal(start.left, traversal)
            traversal += str(start.data) + '-'
            traversal = self.inorder_traversal(start.right, traversal)
        return traversal

    def postorder_traversal(self, start, traversal):
        # left -> right -> root
        if start:
            traversal = self.postorder_traversal(start.left, traversal)
            traversal = self.postorder_traversal(start.right, traversal)
            traversal += str(start.data) + '-'
        return traversal


    # def insert(self, data):
        # if self.data:
        #     if data < self.data:
        #         if self.left is None:
        #             self.left = BST(data)
        #         else:
        #             self.left.insert(data)
        #     elif data > self.data:
        #         if self.right is None:
        #             self.right = BST(data)
        #         else:
        #             self.right.insert(data)
        # else:
        #     self.data = data
        # if self.data:
            # if data <= self.data:
            #     if self.left is None:
            #         self.left = BST(data)
            #     elif data <= self.left.data:
            #         self.left.insert(data)
            #     elif self.right is None:
            #         self.right = BST(data)
            #     else:
            #         self.left.right.insert(data)
            # elif data >= self.data:
            #     if self.right is None:
            #         self.right = BST(data)
            #     elif data >= self.right.data:
            #         self.right.insert(data)
            #     elif self.left is None:
            #         self.left = BST(data)
            #     else:
            #         self.left.insert(data)
            # else:
            #     self.data = data


'''
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

print("preorder " + obj.print_tree("preorder"))
print("inorder " + obj.print_tree("inorder"))
print("postorder " + obj.print_tree("postorder"))

# obj = BST(10)
# obj.insert(4)
# obj.insert(2)
# obj.insert(3)
# obj.insert(6)
# obj.insert(8)
# obj.insert(7)
# obj.insert(5)
# obj.insert(13)
# obj.insert(15)
# obj.insert(17)
# obj.insert(16)
# obj.insert(18)
# obj.insert(19)
# obj.insert(20)
# obj.print_tree()


