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

    # Delete complete double link list
    def delete_all_dll(self):
        ''' We have to update all the previous refrences of nodes to null
        so it will collect garbage '''
        if self.head is None:
            print("Empty double link list")
        else:
            node = self.head
            while node:
                node.previous = None
                node = node.next
            self.head = None
            self.tail = None
            print("deleted")











dll = DoubleLinkList()
dll.createDLL(1)
dll.insert(12,0)
dll.insert(11,0)
dll.insert(32,1)
print([node.value for node in dll])

# dll.delete(1)
# print([node.value for node in dll])
# dll.traverDll()
# dll.reversetraverDll()
# dll.search(32)
# dll.delete_all_dll()

# Practice 27-july-2025

class Node:
    def __init__(self, value):
        self.next = None
        self.previous = None
        self.value = value


class DoubleLinkList:
    def __init__(self):
        self.head=None
        self.tail=None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next


    def createDLL(self, value):
        node = Node(value)
        self.head = node
        self.tail = node
        return node



    def traverse(self):
        if not self.head:
            print("empty")
        node = self.head
        while node:
            print(node.next)
            node = node.next


    def insert_dll(self, location, value):
        if self.head is None:
            node = self.createDLL(value)
            return node

        new_node = Node(value)
        if location == 0:
            node=self.head
            new_node.next = node
            self.head = new_node
            node.previous=new_node
            return new_node

        elif location == 1:
            new_node.next = None
            new_node.previous = self.tail
            self.tail.next = new_node
            self.tail=new_node
            return new_node

        else:
            index = 0
            current_node = self.head
            while index < location:
                current_node=current_node.next
                index += 1

            new_node.next = current_node
            new_node.previous=current_node.previous
            current_node.previous.next= new_node
            current_node.previous=new_node
            return new_node

    def traverse_dll(self):
        list_of_nodes= list()
        node = self.head
        while node:
            # print(node.value)
            list_of_nodes.append(node.value)
            node=node.next
        return list_of_nodes

    def reverse_traverse_dll(self):
        node = self.tail
        reverse_list=list()
        while node:
            reverse_list.append(node.value)
            node = node.previous
        return reverse_list

    def search_dll(self,value):
        node = self.head
        index = 0
        while node:
            if node.value == value:
                print(node.value)
                print(f"found at {index}")
                return node
            node = node.next
            index += 1

    def delete_dll(self,location):
        if self.head is None:
            return f"nothing to delete"

        if location == 0:
            node = self.head
            self.head = node.next
            node.next.previous = self.head
            return f"sdd"

        elif location == 1:
            last = self.tail
            self.tail = last.previous
            last.previous.next = None
            return f"asd"

        else:
            index = 0
            tempnode = self.head
            while index < location -1:
                tempnode = tempnode.next
                index += 1
            tempnode.next = tempnode.next.next
            tempnode.next.previous = tempnode



DLL = DoubleLinkList()
DLL.createDLL(4)
DLL.insert_dll(0,5)
DLL.insert_dll(1,6)
DLL.insert_dll(2,7)
DLL.insert_dll(3,8)
DLL.insert_dll(1,9)

print(DLL.traverse_dll())
DLL.delete_dll(3)
print(DLL.traverse_dll())

print(DLL.reverse_traverse_dll())
DLL.search_dll(8)

print([node.value for node in DLL])