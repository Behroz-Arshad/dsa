class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class CircularLinkList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            if node.next == self.head:
                break
            node = node.next

    def length(self):
        node = self.head
        last = self.tail
        count = 0
        while node:
            if node == last:
                count += 1
                break
            node = node.next
            count += 1

        return count

    def createCSLL(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
            node.next = node
        return "Created"

    def insert(self, value, location = None):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
            node.next = node
        else:
            if location == 0 :
                node.next = self.head.next
                self.head = node
                self.tail.next = node

            elif location == 1:
                node.next = self.tail.next
                self.tail.next = node
                self.tail = node
            else:
                tempNode = self.head
                index = 0
                while index < location-1:
                    tempNode = tempNode.next
                    index += 1

                nextNode = tempNode.next
                tempNode.next = node
                node.next = nextNode

    def traverCll(self):
        node = self.head
        while node:
            print(node.value)
            node = node.next
            if node == self.tail.next:
                break





    def deleteCll(self, location):
        if self.head is None:
            return "Empty"
        if location > self.length() or location < 0:
            return "Invalid"

        if location == 0:
            if self.head == self.tail:
                self.head = None
                self.tail = None
                self.tail.next = None
            else:
                self.head = self.head.next
                self.tail.next = self.head
        elif location == 1:
            temp_node=self.head
            while self.tail.next == self.head:
                if temp_node.next == self.tail:
                    break
                temp_node = temp_node.next

            temp_node.next = self.tail.next
            self.tail = temp_node
            print("value", temp_node.value)
        else:
            index = 0
            previous_node = self.head
            while index < location - 1:
                previous_node = previous_node.next
                index += 1
            want_to_delete_node = previous_node.next
            next_node_of_delete_node = want_to_delete_node.next
            previous_node.next = next_node_of_delete_node





cll = CircularLinkList()
# cll.createCSLL(0)
cll.insert(0,0)
cll.insert(1,1)
cll.insert(2,1)
cll.insert(3,1)
cll.insert(4,1)
cll.insert(5,1)
cll.insert(6,1)

# cll.insert(22,4)
# cll.deleteCll(0)
print([node.value for node in cll])
cll.deleteCll(4)
print([node.value for node in cll])




