class Inventory:
    def __init__(self, initialItems={}):
        self.item_keys = ('Dagger', 'Sword', 'Hammer', 'Coins')
        self.default_items = {'Dagger': 0, 'Sword': 0, 'Hammer': 0, 'Coins': 0}
        self.items = {**self.default_items}
        self.add_items(initialItems)

    def add_item(self, item, qty):
        if item in self.item_keys:
            self.items[item] += qty

    def add_items(self, items={}):
        for item in items:
            self.add_item(item, items[item])

    def remove_item(self, item, qty):
        if item in self.item_keys:
            qty = self.items[item] if self.items[item] < qty else qty
            self.items[item] -= qty

    def remove_items(self, items={}):
        for item in items:
            self.remove_item(item, items[item])

    def print_item_keys(self):
        print()
        print('===| Available Items |===')
        for key in self.item_keys:
            print(key)
        else:
            print('===| No more items! |===')
        print()

    def print_inventory(self):
        print()
        print('===| Inventory |===')
        for item in self.items:
            print(item + ': ' + str(self.items[item]))
        else:
            print('===| No more items! |===')
        print()
