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
        if value < self.value:
            if self.left:
                return self.left.insert(value)
            else:
                self.left = BSTNode(value)
        else:
            if self.right:
                return self.right.insert(value)
            else:
                self.right = BSTNode(value)



    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):

        if self.value == target:
            return self.value
        elif target < self.value and self.left:
            return self.left.contains(target)
        elif target > self.value and self.right:
            return self.right.contains(target)
        # elif target < self.data and self.left
#the original runtime of this code was quadratic time.
import time

import sys

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

sys.path.append('./binary_search_tree')
start_time = time.time()
f = open('names_1.txt', 'r')
duplicates = []  # Return the list of duplicates in this data structure
bst = BSTNode('')
for name_1 in names_1:
    bst.insert(name_1)
for name_2 in names_2:
    if bst.contains(name_2):
        duplicates.append(name_1)
end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")

