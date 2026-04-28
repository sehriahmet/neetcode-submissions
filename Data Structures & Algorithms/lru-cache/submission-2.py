class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0 
        self.hmap = {} 

        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def removeNode(self, node):
        p = node.prev
        n = node.next
        n.prev = p
        p.next = n

    def addToEnd(self, node):
        lastNode = self.tail.prev
        lastNode.next = node
        node.prev = lastNode
        self.tail.prev = node
        node.next = self.tail

    def get(self, key: int) -> int:
        if key in self.hmap:
            node = self.hmap[key]
            self.removeNode(node)
            self.addToEnd(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hmap:
            node = self.hmap[key]
            node.value = value
            self.removeNode(node)
            self.addToEnd(node)
        else:
            node = ListNode(key, value)
            self.hmap[key] = node
            self.addToEnd(node)

            if len(self.hmap) > self.capacity:
                first = self.head.next
                self.removeNode(first)
                del self.hmap[first.key]



class ListNode:
    def __init__(self, key = 0, value = 0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

