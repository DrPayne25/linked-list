class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def insert(self, value):
        new_node = Node(value)
        # if self.head is not None:
        new_node.next = self.head
        self.head = new_node

    def includes(self, value):
        starting = self.head
        while starting != None:
            if starting.value == value:
                return True
            starting = starting.next
        return False

    def to_string(self):
        starting = self.head
        str_result = ''
        while starting != None:
            str_result += starting.getdata()


