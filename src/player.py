# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room, inventory=[]):
        self.name = name
        self.current_room = current_room
        self.inventory = inventory

    def __str__(self):
        output = ""
        output += f"You,{self.name}, have {len(self.inventory)} items in your inventory"
        inventoryNumber = 1
        for e in self.inventory:
            output += f"{inventoryNumber}. {e.name} - {e.description}"
            inventoryNumber += 1
        return output