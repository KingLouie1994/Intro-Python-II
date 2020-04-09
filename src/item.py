class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def took_item(self):
        print(f"\n***You added {self.name} to your inventory***")

    def dropped_item(self):
        print(f"\n***You removed {self.name} from your inventory***")