class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def insertSLL(self, value, location):
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
            while index < location - 1:
                tempNode = tempNode.next
                index += 1
            nextNode = tempNode.next
            tempNode.next = new_node
            new_node.next = nextNode

    def traverseLinkList(self):
        if self.head is None:
            print("Empty")
        else:
            node = self.head
            while node:
                print(node.value)
                node = node.next

    def deleteSLL(self, location):
        node = self.head
        if self.head is None:
            return "Empty list"

        if location == 0:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = node.next
        elif location == 1:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                node = self.head
                while node is not None:
                    if node.next == self.tail:
                        break
                    node = node.next
                node.next = None
                self.tail = node
        else:
            tempNode = self.head
            index = 0
            while index < location - 1:
                tempNode = tempNode.next
                index += 1
            nextNode = tempNode.next
            tempNode.next = nextNode.next





    def search(self, value):
        node = self.head
        while node:
            if node.value == value:
                return node.value
            node = node.next
        return "Not matched"

    def delete_full_SLL(self):
        if self.head is None:
            return "Empty"

        self.head = None
        self.tail = None


'''
if return 
1,2,3,4,5
0,1,2,3,4

'''




single_linklist = LinkedList()

single_linklist.insertSLL(0, 0)
single_linklist.insertSLL(1, 1)
single_linklist.insertSLL(2, 1)
single_linklist.insertSLL(3, 1)
single_linklist.insertSLL(4, 1)
single_linklist.insertSLL(99, 1)

# single_linklist.head = n1
# single_linklist.head.next = n2
# single_linklist.tail = n2


print([node.value for node in single_linklist])

# single_linklist.traverseLinkList()
# print(single_linklist.search(43))
single_linklist.deleteSLL(23)
# single_linklist.delete_full_SLL()
print("-------------")
print([node.value for node in single_linklist])
