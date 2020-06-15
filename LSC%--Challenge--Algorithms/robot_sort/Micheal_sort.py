# Check if we can move right
if self.can_move_right() is False:
    return self._list

# Swap the item
self.swap_item()

# Move to the right while we can
while self.can_move_right() is True:
    self.move_right()

    # Swap if we need to
    if self.compare_item() == 1:
        self.swap_item()

# Move to the left while we can
while self.can_move_left() is True:
    self.move_left()

    # Swap if we need to
    if self.compare_item() == None:
        self.swap_item()
        break

# Move to the Right
self.move_right()
# Recursivly call ourself
self.sort()
if __name__ == "__main__":

    robot = SortingRobot(l)
    robot.sort()
    print(robot._list)
