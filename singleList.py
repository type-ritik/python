class ListNode:
    def __init__(self, value):
        self.data = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def add(self, data):
        new_node = ListNode(data)
        if self.head is None:
            self.head = new_node
        else:
            curr_node = self.head
            while curr_node.next is not None:
                curr_node = curr_node.next
            curr_node.next = new_node
        self.length = self.length + 1

    def print(self):
        curr_node = self.head
        while curr_node:
            print(curr_node.data, end="->")
            curr_node = curr_node.next
        print("None")


ll = LinkedList()
ll.add(5)
ll.add(10)
ll.add(25)
ll.add(30)
ll.print()
