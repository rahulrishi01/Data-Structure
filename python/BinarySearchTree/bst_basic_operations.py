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
            node = self._find(data, self.root)
            if node:
                return node
            else:
                return None
        else:
            return None

    def _find(self, data, curr_node):
        if data < curr_node.key and curr_node.left:
            return self._find(data, curr_node.left)
        elif data > curr_node.key and curr_node.right:
            return self._find(data, curr_node.right)
        if data == curr_node.key:
            return curr_node

    def delete(self, data):
        if self.root:
            self.root = self._delete(data, self.root)

    def _delete(self, data, curr_node: Node):
        # If the key to be deleted is smaller than the root's key then it lies in  left subtree
        if data < curr_node.key:
            curr_node.left = self._delete(data, curr_node.left)

        # If the kye to be delete is greater than the root's key then it lies in right subtree
        elif data > curr_node.key:
            curr_node.right = self._delete(data, curr_node.right)

        # If key is same as root's key, then this is the node to be deleted
        else:
            # Node with only one child or no child
            if curr_node.left is None:
                return curr_node.right
            elif curr_node.right is None:
                return curr_node.left
            else:
                # inorder sucessor of the tree
                succ_node = self.find_min(curr_node.right)
                curr_node.key = succ_node.key
                curr_node.right = self._delete(succ_node.key, curr_node.right)
        return curr_node

    def find_min(self, curr_node: Node):
        if curr_node:
            while curr_node.left is not None:
                curr_node = curr_node.left
        return curr_node

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

    def _levelorder_traversal(self, start: Node, traversal):
        pass

    #   longest path from the root node to a leaf node
    def bst_height(self):
        if self.root is None:
            return 0
        else:
            return self._bst_height(self.root)

    def _bst_height(self, curr_node):
        if curr_node is None:
            return 0
        else:
            return 1 + max(self._bst_height(curr_node.left), self._bst_height(curr_node.right))

    # The size of a binary tree is the total number of nodes in that tree.
    def bst_size(self):
        if self.root is None:
            return 0
        else:
            return self._bst_size(self.root)

    def _bst_size(self, curr_node: Node):
        if curr_node is None:
            return 0
        else:
            return 1 + self._bst_size(curr_node.left) + self._bst_size(curr_node.right)

    # The depth of a node is the number of edges from the node to the tree's root node.
    def node_depth(self, data):
        pass

    def k_th_smallest(self, k):
        if k is None or self.root is None:
            return None
        else:
            min_val, k = self._k_th_smallest(self.root, None, k)
            if k != 1:
                print("Not Found")
            else:
                print("Minimum value {}".format(min_val))

    def _k_th_smallest(self, start, data, k):
        if start:
            data, k = self._k_th_smallest(start.left, data, k)
            if k == 1:
                if data is None:
                    data = start.key
                return data, k
            else:
                k = k - 1
            data, k = self._k_th_smallest(start.right, data, k)
        return data, k

    def kthSmallest(self, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """

        def inorder(r: Node):
            return inorder(r.left) + [r.key] + inorder(r.right) if r else []

        return inorder(self.root)[k - 1]

    def kthSmallest_itr(self, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        stack = []
        current = self.root

        while True:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            k -= 1
            if not k:
                return current.key
            current = current.right

    def kthLargest_itr(self, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        stack = []
        current = self.root

        while True:
            while current:
                stack.append(current)
                current = current.right
            current = stack.pop()
            k -= 1
            if not k:
                return current.key
            current = current.left

    def inorder_successor(self, p: Node):
        root = self.root
        successor = None

        while root != None and root.key != p.key:
            if root.key > p.key:
                successor = root
                root = root.left
            else:
                root = root.right

        if root == None:
            return None

        if root.right == None:
            return successor

        root = root.right
        while root.left != None:
            root = root.left
        return root

    def inorder_predecessor(self):
        pass


if __name__ == '__main__':
    bst = BST()
    bst.insert(20)
    bst.insert(8)
    bst.insert(22)
    bst.insert(4)
    bst.insert(12)
    bst.insert(10)
    bst.insert(14)
    # bst.insert(5)
    # bst.insert(2)
    # bst.insert(9)
    # print(bst.find(4))
    # print(bst.find(1))
    print(bst.print_tree("preorder"))
    print(bst.print_tree("postorder"))
    # bst.delete(2)
    print(bst.print_tree("inorder"))
    # print(bst.kthSmallest(3))
    # print(bst.kthLargest_itr(8))
    # print(bst.kthSmallest_itr(3))
    node = bst.find(8)
    req_node = bst.inorder_successor(node)
    if req_node:
        print(req_node.key)
    else:
        print("None")
    # bst.k_th_smallest(5)
    print("Size of Binary search tree is: {}".format(bst.bst_size()))
    print("Height of Binary search tree is: {}".format(bst.bst_height()))




