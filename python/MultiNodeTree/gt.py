from queue import Queue


class Node():
    """ Node class for general tree implementation
    Instance functions:
    - add_child
    - preorderTraversal
    - breadthFirstTraversal
    """

    def __init__(self, node_id):

        """setup logging, attach logger to handlers and instatiante Node  """
        self.node_children = []
        self.node_id = node_id

    def __str__(self):

        """ return node_id"""
        return self.node_id

    def add_child(self, child):

        """Instance function to add node to parent"""
        # add child to parent
        self.node_children.append(child)

    def preorderTraversal(self, preorder_list):

        """Traverse a general tree in preorder. Entry point the invoking node.
        Each node traversed is appended to a list

        Parameters: preorder_list Type list: element Type Node()
        Return: list of nodes traversed in preorder"""
        # add node to list preorder_list
        preorder_list.append(self)
        # recursively call self for each of node node_children
        for i in self.node_children:
            i.preorderTraversal(preorder_list)

        # once all nodes have been visited return list of nodes in preorder
        return preorder_list

    def breadthFirstTraversal(self, node_queue, visited):
        """ Traverse gerneral tree breadth first order, return ordered list"""

        # self has been visited add node to list
        visited.append(self)

        # build the queue
        for i in self.node_children:
            node_queue.put(i)

        # process the queue
        while node_queue.qsize() != 0:
            return node_queue.get().breadthFirstTraversal(node_queue, visited)

        # base case empty queue
        return visited


def main():
    # create nodes
    root = Node('root')
    node1 = Node('node1')
    node2 = Node('node2')
    node3 = Node('node3')
    node4 = Node('node4')
    node5 = Node('node5')
    node6 = Node('node6')
    node7 = Node('node7')
    node8 = Node('node8')
    node9 = Node('node9')
    node10 = Node('node10')
    node11 = Node('node11')

    # add nodes to parent
    root.add_child(node1)
    root.add_child(node2)
    root.add_child(node3)
    node1.add_child(node4)
    node4.add_child(node5)
    node4.add_child(node6)
    node4.add_child(node7)
    node5.add_child(node11)
    node3.add_child(node8)
    node8.add_child(node9)
    node8.add_child(node10)

    # root
    # node1  node2   node3
    # node4              #node8
    # node5, node6, node7    node9, node10
    # node11

    # list for traversal results
    visited = []

    # queue to pass to breadth first traversal function
    gTree_queue = Queue()

    # invoke breadthFirstTraversal passing empty queue & list
    visited = node4.breadthFirstTraversal(gTree_queue, visited)

    print('breadthFirstTraversal')
    for i in visited:
        print(i)
    print('preorderTraversal')
    visited.clear()

    # invoke preorderTraversal passing empty list
    visited = node4.preorderTraversal(visited)
    for i in visited:
        print(i)


if __name__ == '__main__':
    main()
