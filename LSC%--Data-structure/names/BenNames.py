"""
Binary search trees are a data structure that enforce an ordering over
the data they store. That ordering in turn makes it a lot more efficient
at searching for a particular piece of data in the tree.
This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # create a BSTNode to use later
        new_node = BSTNode(value)

        # do our first split, we are storing smaller values to the left
        if self.value > value:

            # we have to potential conditions on either leg
            # 1. There is a value here
            #   - If a value is present, run the insert method of that node
            #   to continue the process recursively
            if self.left:
                return self.left.insert(value)

            # 2. If we don't have a value, we can go ahead and just
            # set it to the node we have created
            else:
                self.left = new_node

        # This else will follow the right side and reflect
        else:
            if self.right:
                return self.right.insert(value)
            else:
                self.right = new_node

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # if the target is the current value
        # we are done looking :D
        if target == self.value:
            return True

        # we know we are storing lesser values left,
        # if the target is lower than the value, we know
        # we need to go left
        elif target < self.value:

            # if a node is present on the left side
            # recursively return the contains method on that node
            if self.left:
                return self.left.contains(target)

            # if we have reached the end of the left tail
            # it does not exist in here
            else:
                return False

        # assuming target is higher, move right and mirror
        else:
            if self.right:
                return self.right.contains(target)
            else:
                return False

import time
import sys
sys.path.append('./binary_search_tree')
f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

start_time = time.time()
duplicates = []  # Return the list of duplicates in this data structure
bst = BSTNode("")
for name_1 in names_1:
    bst.insert(name_1)
for name_2 in names_2:
    if bst.contains(name_2):
        duplicates.append(name_2)
end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")