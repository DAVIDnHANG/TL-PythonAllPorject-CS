# Implement a class to hold room information. This should have name and
# description attributes.

class Room():
    def __init__(self, Player, description):
        self.Player = Player
        self.description = description
        self.list_items=[]
        self.inventory=[]

        self.name = Player
        self.description=  description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.holding = []

    def get_inventory(self):
        myString = []
        for thingy in self.inventory:
            myString.append(str(thingy.name))
        return ', '.join(myString)

    def check_item(self, item):
        if item in self.inventory:
            print("You already have this item!")
        else:
            return False

    def add_item(self, item):
        self.inventory.append(item)
        print(item.on_take(item))

    def remove_item(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            print(item.on_drop(item))
        else:
            print("Impossible! You don't have this item!")

