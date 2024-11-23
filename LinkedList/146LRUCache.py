class Node:
    def __init__(self, key: int, value: int, next= None, prev= None):
        self.key = key
        self.value = value
        self.next = next
        self.prev = prev

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.length = 0        
        self.map = {}
        self.head = None
        self.tail = None
    
    def place_front(self, key: Node) -> int:
        target = self.map[key]
        if target == self.head:
            return target.value
        elif target == self.tail:
            target.prev.next = None
            self.tail = target.prev
        else:
            target.prev.next = target.next
            target.next.prev = target.prev

        target.prev = None
        target.next = self.head
        target.next.prev = target
        self.head = target

        return target.value
    
    def get(self, key: int) -> int:
        if not self.map.get(key):
            return -1

        return self.place_front(key) 

    def put(self, key: int, value: int) -> None:
        if self.map.get(key):
            self.map[key].value = value
            self.place_front(key)
        else:
            node = Node(key, value, self.head, None)
            self.map[key] = node
            if self.length > 0:
                self.head.prev = node
            else:
                self.tail = node
            self.head = node 
            if self.length == self.capacity:
                del self.map[self.tail.key]
                self.tail = self.tail.prev
                self.tail.next = None
            else:
                self.length += 1

