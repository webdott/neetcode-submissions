class Node:
    def __init__(self, key, val, prev = None, nxt = None):
        self.key, self.val = key, val
        self.prev = prev
        self.next = nxt

class LRUCache:
    def __init__(self, capacity: int):
        self.map_ = {}
        self.capacity = capacity
        self.head = Node(0, 0)
        self.tail = Node(0, 0)

        self.head.next, self.tail.prev = self.tail, self.head

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def insert(self, node):
        # prev, nxt = self.head, self.head.next

        # prev.next = nxt.prev = node
        # node.next, node.prev = nxt, self.head
        nxt = self.head.next

        nxt.prev = node
        node.next, node.prev = nxt, self.head
        self.head.next = node


    def get(self, key: int) -> int:
        if key in self.map_:
            node = self.map_[key]

            print(node.val, key, len(self.map_), self.map_)
            self.remove(node)
            self.insert(node)

            return node.val
       
        return -1

    def put(self, key: int, value: int) -> None:
        node = Node(key, value)

        if key in self.map_:
            self.remove(self.map_[key])
        elif len(self.map_) == self.capacity:
            node_to_del = self.tail.prev

            self.remove(node_to_del)
            del self.map_[node_to_del.key]

        self.insert(node)
        self.map_[key] = node
        
