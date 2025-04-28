from operator import index


class Node:
    def __init__(self, value):
        self.next = None
        self.previous = None
        self.value = value


class DoubleLinkList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node=node.next

    def createDLL(self, value:int):
        node = Node(value)
        self.head = node
        self.tail = node
        node.next = None
        node.previous = None
        return f"DLL is created"

    def insert(self, value:int, location=None):
        node = Node(value)
        if location == 0:
            if self.head == None:
                self.head = node
                self.tail = node
                node.next = None
                node.previous = None
            else:
                existing_node = self.head
                node.previous = None
                node.next = existing_node
                existing_node.previous = node
                self.head = node
        elif location == 1:
            node.next=None
            node.previous = self.tail
            self.tail.next = node
            self.tail = node

        else:
            tempNode = self.head
            index = 0
            while index < location-1:
                tempNode = tempNode.next
                index += 1
            node.next = tempNode.next
            node.previous = tempNode
            node.next.previous = node
            tempNode.next = node

    def traverDll(self):
        node = self.head
        if not node:
            print( "empty")
        else:
            while node:
                print(node.value)
                node = node.next


    def reversetraverDll(self):
        node = self.tail
        if not node:
            print( "empty")
        else:
            while node:
                print(node.value)
                node = node.previous


    def search(self, value):
        node = self.head
        while node:
            if value == node.value:
                print("Find value", node.value)
                break
            node = node.next

    # Delete node from double link list

    def delete(self, location):
        if self.head is None:
            print("Empty")
        elif location == 0:
            self.head = self.head.next
            self.head.previous = None
        elif location == 1:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.tail = self.tail.previous
                self.tail.next = None
        else:
            current_node = self.head
            index = 0
            while index < location -1 :
                current_node = current_node.next
                index += 1
            current_node.next = current_node.next.next
            current_node.next.previous = current_node
        print("Node has been deleted")











dll = DoubleLinkList()
dll.createDLL(1)
dll.insert(12,0)
dll.insert(11,0)
dll.insert(32,1)
print([node.value for node in dll])
dll.delete(1)
print([node.value for node in dll])
# dll.traverDll()
# dll.reversetraverDll()
# dll.search(32)
