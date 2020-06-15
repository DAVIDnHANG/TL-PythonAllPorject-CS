# We know we start at index 0 with None in our hands,
# and we need to pick up a number to sort
self.swap_item()

# Give us a loop that we can run until we decide to break
while True:
    # self.move_right() will both move right and return True if it can
    # otherwise will stop. Each time we will compare our item. If it is larger,
    # we are going to swap
    while self.move_right():
        if self.compare_item() >= 1:
            self.swap_item()

    # This is our exit loop check. If we are at the end of the list AND the end is None
    # We consider our list sorted, pick up None and end
    if (self.can_move_right() == False) and (self.compare_item() == None):
        self.swap_item()
        break

    # This is the return trip. Walk all the way back to the start.
    # Pick up None, move right, drop None, break our nested while
    # to return to the top while ( line 105 ) which will begin
    # the process again, moving right
    while self.move_left():
        if self.compare_item() == None:
            self.swap_item()
            self.move_right()
            self.swap_item()
            break