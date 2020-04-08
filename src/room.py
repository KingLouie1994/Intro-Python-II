# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, items=[]):
        self.name = name
        self.description = description
        self.n_to = None
        self.e_to = None
        self.s_to = None
        self.w_to = None
        self.items = items

    def __str__(self):
        output = ""
        output += f"\nYour position: {self.name}\n{self.description}\n"
        itemNumber = 1

        if len(self.items) == 0:
            output += f"\nNo items here - This room is empty!\n"
        else:
            output += "\nItems in the room:\n"
            for e in self.items:
                output += f"{itemNumber}. {e.name} - {e.description}\n"
                itemNumber += 1
        return output