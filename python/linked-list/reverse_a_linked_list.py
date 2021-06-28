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

    def reverse_list_iteretive(self):
        if not self.head:
            print("Linked list is empty")
            return None
        current = self.head
        prev = None
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def reverse_list_recursive(self):
        if self.head is None:
            return
        self._reverse_list_recursive(self.head, None)

    def _reverse_list_recursive(self, curr, prev):
        if curr.next is None:
            self.head = curr
            curr.next = prev
            return 

        next = curr.next
        curr.next = prev

        self._reverse_list_recursive(next, curr)


if __name__ == '__main__':
    l_list = LinkedList()
    l_list.insert(1)
    l_list.insert(2)
    l_list.insert(3)
    l_list.insert(4)
    l_list.insert(5)
    l_list.insert(6)
    l_list.insert(7)
    print("Display before reversing:")
    l_list.display()
    print("After reversing:")
    l_list.reverse_list_iteretive()
    l_list.display()
    print("After recursive reverse:")
    l_list.reverse_list_recursive()
    l_list.display()

