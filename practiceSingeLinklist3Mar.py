class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class SingleLinkList:
    def __init__(self):
        self.head = None
        self.tail = None


    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def insertSLL(self, value, position=None):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        elif position == 0:
            node.next = self.head
            self.head = node
        elif position == 1:
            self.tail.next = node
            self.tail = node

        else:
            tempnode = self.head
            index = 0
            while index < position - 1:
                tempnode = tempnode.next
                index += 1
            node.next = tempnode.next
            tempnode.next = node

    def search(self, value):
        node = self.head
        while node:
            if node.value == value:
                return value
            node = node.next
        return "Not matched"

    def traverse(self):
        node_list = []
        if self.head is None:
            return []
        node = self.head
        while node:
            node_list.append(node.value)
            node = node.next
        return node_list

    def delete_node(self, position = None):
        if self.head is None:
            return "Empty"
        node = self.head
        if position == 0:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = node.next
        elif position == 1:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                node = self.head
                while node:
                    if node.next == self.tail:
                        break
                    node = node.next
                node.next = None
                self.tail = node

    def delete_all_node(self):
        if self.head is None:
            return "Empty link list"
        self.head = None
        self.tail = None
        return "Deleted successfully"



single_linklist = SingleLinkList()

single_linklist.insertSLL(0, 0)
single_linklist.insertSLL(1, 1)
single_linklist.insertSLL(2, 1)

print([node.value for node in single_linklist])
print(single_linklist.search(23))
print(single_linklist.traverse())
print(single_linklist.delete_all_node())
print(single_linklist.traverse())



# operations insert, delete , traverse, search
