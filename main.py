from character import Character
from game import Game
from sequence import cave

character = Character('Joshua', 32, 'Palladin', {'Dagger': 5, 'Sword': 1})
game = Game(character, cave)

print("Hello World!")
character.inventory.print_item_keys()
character.print_character_info()
print("Commencing Game: "+game.path['name']+"...")
game.play()
