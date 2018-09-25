# A Simple Program to Traverse into a Linked List
import sys

# Node class
class Node:

    # Constructor to initialize object.
    def __init__(self, data):
        # print(data)
        self.data = data    # To contain element
        self.next = None    # To address next node

# Linked List
class LinkedList:

    def __init__(self):
        self.head = None

# Create a linked list with 4 nodes
def create_list(llist, data):
    temp_node = None
    for value in data:
        node = Node(value)
        if temp_node:
            temp_node.next = node
        else:
            llist.head = node
        temp_node = node

# Traverse and print each item into the linked list
def traverse_list(llist):
    temp = llist.head
    while(temp):
        print(temp.data)
        temp = temp.next

# The main function
if __name__ == "__main__":
    print("Enter elements separated by space")
    data = sys.stdin.readline().strip()
    data = data.split(' ')
    llist = LinkedList()
    create_list(llist, data)
    traverse_list(llist)