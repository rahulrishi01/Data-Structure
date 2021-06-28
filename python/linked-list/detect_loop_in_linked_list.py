class newNode:
    def __init__(self, key):
        self.key = key
        self.next = None


# A utility function to pra linked list
def printList(head):
    while (head != None):
        print(head.key, end=" ")
        head = head.next


# Function to detect first node of loop
# in a linked list that may contain loop
def detectLoop(head: newNode) -> bool:
    if not head:
        return False
    slow_ptr = head
    fast_ptr = head.next
    loop_flag = 0
    while fast_ptr and fast_ptr.next:
        if slow_ptr == fast_ptr:
            loop_flag = 1
            break
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next.next
    if loop_flag:
        return True
    else:
        return False

def removeLoop(head: newNode):
    if not head:
        return False
    slow_ptr = head
    fast_ptr = head.next
    loop_flag = 0
    while fast_ptr and fast_ptr.next:
        if slow_ptr == fast_ptr:
            loop_flag = 1
            break
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next.next
    if loop_flag:
        loop_ptr = fast_ptr
        while loop_ptr.next != fast_ptr and loop_ptr.next != head:
            loop_ptr = loop_ptr.next
        loop_ptr.next = None
    print("Loop removed")


if __name__ == '__main__':
    # Driver Code
    head = newNode(1)
    head.next = newNode(2)
    head.next.next = newNode(3)
    head.next.next.next = newNode(4)
    head.next.next.next.next = newNode(5)
    printList(head)

    # Create a loop for testing(5 is pointing to 3)
    head.next.next.next.next.next = head.next.next

    found = detectLoop(head)
    if (found):
        print("Loop Found")
        removeLoop(head)
    else:
        print("No Loop")
    print("Again checking for loop")
    found = detectLoop(head)
    if (found):
        print("Loop Found")
    else:
        print("No Loop")
    printList(head)