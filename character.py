from inventory import Inventory


class Character:
    def __init__(self, name, age, character_class, inventory={}):
        self.name = name
        self.age = age
        self.character_class = character_class
        self.inventory = Inventory(inventory)

    def print_character_info(self):
        print()
        print("===| Character Information |===")
        print("Name: " + self.name)
        print("Age: " + str(self.age))
        print("Class: " + self.character_class)
        print()
        print("========================================")
        self.inventory.print_inventory()
        print("========================================")
        print()
