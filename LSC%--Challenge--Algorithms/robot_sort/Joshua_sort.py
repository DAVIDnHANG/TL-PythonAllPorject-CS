# the robot starts at the beginning of the list with None in hand. pick up the item at the starting index so we can compare it to other numbers.
self.swap_item()

# while we're holding the item we will be doing numerous things, this will be handled in a loop

while True:
    # being that we started all the way left on the list we will move right. As we're moving right we'll compare the number we're holding to the number at the next index.
    while self.move_right():
        # once we get to an item that is less than what we're holding we'll swap them.
        if self.compare_item() >= 1:
            self.swap_item()

    # once we're finished, that means we'll be at the last index and we need to be holding None
    if (self.can_move_right() == False) and (self.compare_item() == None):
        self.swap_item()
        break

    # if we don't meet the conditions for the if, that means we got to the far right and are not complete, we now walk left until we reach None. None will always be at the
    # index we want to put the lowest current value in the list. We then swap our current (and lowest) number with None, move right, switch None with a number and break
    # this loop, returning to a previous loop
    while self.move_left():
        if self.compare_item() == None:
            self.swap_item()
            self.move_right()
            self.swap_item()
            break

if __name__ == "__main__":