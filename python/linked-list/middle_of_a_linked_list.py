class Node:
    def __init__(self, data):
        self.next = None
        self.data = data


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)

    def display(self):
        if self.head:
            currnet = self.head
            while currnet:
                print(currnet.data, "==>")
                currnet = currnet.next
        else:
            print("Linked list is empty")


def middle_of_linked_list(head: Node):
    if not head:
        print("Linked list is empty")
        return None
    slow_ptr = head
    fast_ptr = head
    while fast_ptr and fast_ptr.next:
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next.next
    return slow_ptr.data


def middle_of_linked_list_2(head: Node):
    if not head:
        print("Linked list is empty")
        return None
    current = head
    counter = 0
    mid = current
    while current:
        if counter & 1:
            mid = mid.next
        counter += 1
        current = current.next
    return mid.data


if __name__ == '__main__':
    l_list = LinkedList()
    l_list.insert(1)
    l_list.insert(2)
    l_list.insert(3)
    l_list.insert(4)
    l_list.insert(5)
    l_list.insert(6)
    l_list.insert(7)
    l_list.display()
    middle = middle_of_linked_list(l_list.head)
    print("Middle of the linked list is : {}".format(middle))
    middle = middle_of_linked_list_2(l_list.head)
    print("Middle of the linked list is : {}".format(middle))
