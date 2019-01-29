'''
Program to make a BST with a method to find width at each level.
'level' attribute is optional and can be removed if not required in any other functionality.
'''


class Node:
    counter = 0
    # Level 0 width is set explicitly as we won't be using insert method for root of Tree.
    width = {0: 1}

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.level = 0  # Optional for finding width using this approach

    def insert(self, data):
        if data < self.data:
            Node.counter += 1
            if self.left is None:
                self.left = Node(data)
                self.left.level = Node.counter
                if Node.counter in Node.width:
                    Node.width[Node.counter] += 1
                else:
                    Node.width[Node.counter] = 1
                Node.counter = 0
            else:
                self.left.insert(data)
        else:
            Node.counter += 1
            if self.right is None:
                self.right = Node(data)
                self.right.level = Node.counter
                if Node.counter in Node.width:
                    Node.width[Node.counter] += 1
                else:
                    Node.width[Node.counter] = 1
                Node.counter = 0
            else:
                self.right.insert(data)

    def print_tree(self):
        if self.left is not None:
            self.left.print_tree()
        print(f'{self.data}', end=' ')
        if self.right is not None:
            self.right.print_tree()


root = Node(10)
root.insert(21)
root.insert(5)
root.insert(19)
root.insert(1)
root.insert(6)
root.insert(20)
root.insert(22)
root.insert(23)
root.insert(24)
print('Tree : ', end='')
root.print_tree()
print('\nWidth of Tree at each level :', root.width)

'''
Output :
Tree : 1 5 6 10 19 20 21 22 23 24
Width of Tree at each level : {0: 1, 1: 2, 2: 4, 3: 2, 4: 1}
'''
