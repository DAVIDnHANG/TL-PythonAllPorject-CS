What happens to new_node.prev?


def add_to_head(self,value):
    new_node = ListNode(value)
    self.length += 1
    if self.head:
        new_node.next = self.head
        self.head.prev = new_node
    else:
        self.tail = new_node
    self.head=new_node