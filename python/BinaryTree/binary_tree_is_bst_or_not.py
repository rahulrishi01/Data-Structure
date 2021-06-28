class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        stack = []
        current = root
        prev = None
        while stack or current:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            if prev and current.val <= prev.val:
                return False
            prev = current
            current = current.right
        return True

def check_bst(root: Node, min, max):
    if root is None:
        return True
    if root.data < min or root.data > max:
        return False
    return check_bst(root.left, min, root.data) and check_bst(root.right, root.data, max)


if __name__ == '__main__':
    root = Node(3)
    root.left = Node(2)
    root.right = Node(5)
    root.right.left = Node(4)
    root.right.right = Node(1)
    min = -9999999
    max = 9999999
    if check_bst(root, min, max):
        print("Tree is BST")
    else:
        print("Tree is not BST")
