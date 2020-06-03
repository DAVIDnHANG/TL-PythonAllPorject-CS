
import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Queue:
    def __init__(self):
        self.size = 0
        self.storage = DoublyLinkedList()

    def __len__(self):
        return self.storage.length
    def enqueue(self, value):
        return self.storage.add_to_tail(value)
        
    def dequeue(self):
        return self.storage.delete(self.storage.head)
    
'''

class Queue:
    def __init__(self):
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        self.storage.add_to_tail(value)

    def dequeue(self):
        if self.len() == 0:
            return None
        return self.storage.remove_from_head()

    def len(self):
        return len(self.storage)
'''