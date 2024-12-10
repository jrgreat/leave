class Node(object):
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree(object):
    def insert(self, root, value):
        if root == None:
            root = Node(value)
        elif root.value < value:
            root.right = self.insert(root.right, value)
        elif root.value > value:
            root.left = self.insert(root.left, value)
        return root

    def query(self, root, value):
        if root == None:
            return None
        if root.value == value:
            return root
        elif value < root.value:
            return self.query(root.left, value)
        elif value > root.value:
            return self.query(root.right, value)

    def printTree(self, root):
        if root == None:
            return
        self.printTree(root.left)
        print(root.value, end=' ')
        self.printTree(root.right)

if __name__=="__main__":
    List = [17,5,35,2,11,29,38,9,16,8]
    root = None
    tree = BinarySearchTree()
    for val in List:
        root = tree.insert(root, val)
    tree.printTree(root)
    node = tree.query(root, 16)
    print(node)
    print(node.value)



def average_weight(s):
    char_list = s.split(' ')
    sum = 0
    for word in char_list:
        sum = sum + len(word)
    return sum / len(char_list)

