class Node:
    def __init__(self, data=None):
        self.left = None
        self.right = None
        self.key = data


class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, curr_node):
        if data < curr_node.key:
            if curr_node.left is None:
                curr_node.left = Node(data)
            else:
                self._insert(data, curr_node.left)
        elif data > curr_node.key:
            if curr_node.right is None:
                curr_node.right = Node(data)
            else:
                self._insert(data, curr_node.right)
        else:
            print("{} is already present in the BST.")

    def find(self, data):
        if self.root:
            is_found = self._find(data, self.root)
            if is_found:
                return True
            else:
                return False
        else:
            return None

    def _find(self, data, curr_node):
        if data < curr_node.key and curr_node.left:
            return self._find(data, curr_node.left)
        elif data > curr_node.key and curr_node.right:
            return self._find(data, curr_node.right)
        if data == curr_node.key:
            return True

    def delete(self, data):
        pass

    def _delete(self, data):
        pass

    def print_tree(self, traversal_type):
        if traversal_type == 'preorder':
            return self._preorder_traversal(self.root, "")
        elif traversal_type == 'inorder':
            return self._inorder_traversal(self.root, "")
        elif traversal_type == 'postorder':
            return self._postorder_traversal(self.root, "")
        else:
            print("Traversal type {} is not supported".format(traversal_type))

    def _preorder_traversal(self, start: Node, traversal: str):
        if start:
            traversal = traversal + " - " + str(start.key)
            traversal = self._preorder_traversal(start.left, traversal)
            traversal = self._preorder_traversal(start.right, traversal)
        return traversal

    def _postorder_traversal(self, start: Node, traversal: str):
        if start:
            traversal = self._postorder_traversal(start.left, traversal)
            traversal = self._postorder_traversal(start.right, traversal)
            traversal = traversal + " - " + str(start.key)
        return traversal

    def _inorder_traversal(self, start: Node, traversal: str):
        if start:
            traversal = self._inorder_traversal(start.left, traversal)
            traversal = traversal + " - " + str(start.key)
            traversal = self._inorder_traversal(start.right, traversal)
        return traversal


if __name__ == '__main__':
    bst = BST()
    bst.insert(7)
    bst.insert(4)
    bst.insert(12)
    bst.insert(6)
    bst.insert(10)
    bst.insert(3)
    bst.insert(8)
    bst.insert(5)
    bst.insert(2)
    bst.insert(9)
    print(bst.find(4))
    print(bst.find(1))
    print(bst.print_tree("preorder"))
    print(bst.print_tree("postorder"))
    print(bst.print_tree("inorder"))




