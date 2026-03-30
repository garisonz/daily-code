class LinkedNode:

    def __init__(self, value: int, next = None):
        self.value = value
        self.next = next

class LinkedList:

    def __init__(self):
        self.head = LinkedNode(-1)
        self.tail = self.head

    def get(self, i: int) -> int:
        curr = self.head.next
        index = 0
        while curr:
            if index == i:
                return curr.value
            index += 1
            curr = curr.next
        return -1

    def insertHead(self, val) -> None:
        new_node = LinkedNode(val, self.head.next)
        self.head.next = new_node
        if self.head == self.tail:
            self.tail = new_node

    def insertTail(self, val: int) -> None:
        new_node = LinkedNode(val)
        self.tail.next = new_node
        self.tail = new_node

    def remove(self, i: int) -> bool:
        curr = self.head
        index = 0

        while curr and curr.next:
            if index == i:
                if curr.next == self.tail:
                    self.tail = curr
                curr.next = curr.next.next
                return True
            index += 1
            curr = curr.next
        return False

    def getValues(self):
        vals = []
        curr = self.head.next
        while curr:
            vals.append(curr.value)
            curr = curr.next
        return vals