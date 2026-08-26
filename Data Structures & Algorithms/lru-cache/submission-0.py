class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
         # initialise LRUCache with capacity 
        self.size = capacity
        self.LRUCache = {}

        # dummy node
        self.old = Node(0, 0)
        self.new = Node(0, 0)

        self.old.next = self.new
        self.new.prev = self.old

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def insert(self, node):
        before = self.new.prev

        before.next = node
        node.prev = before

        node.next = self.new
        self.new.prev = node
  

    def get(self, key: int) -> int:
        # if key in cache return value
        if key not in self.LRUCache:
            return -1
        
        node = self.LRUCache[key]
        self.remove(node)
        self.insert(node)
        
        return node.val

    def put(self, key: int, value: int) -> None:
        # if key exists update value
        if key in self.LRUCache:
            node = self.LRUCache[key]
            self.remove(node)
            
            update = Node(key,value)
            self.LRUCache[key] = update
            self.insert(update)
        
        else:
            new_node = Node(key,value)
            self.LRUCache[key] = new_node
            self.insert(new_node)

            # else add key-value pair
            if (len(self.LRUCache) > self.size):
                old_node = self.old.next

                # remove from linked list
                self.remove(old_node)
                # remove from dictionary
                del self.LRUCache[old_node.key]

    

    
