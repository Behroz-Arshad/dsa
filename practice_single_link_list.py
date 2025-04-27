class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class SingleLinkList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self,value,location=None):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        elif location == 0:
            new_node.next = self.head
            self.head = new_node
        elif location == 1:
            new_node.next = None
            self.tail.next = new_node
            self.tail = new_node
        else:
            tempNode = self.head
            index = 0
            while index < location -1:
                tempNode = tempNode.next
                index += 1
            next_node = tempNode.next
            tempNode.next = new_node
            new_node.next = next_node

