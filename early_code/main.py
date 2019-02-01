from room import Room
from item import Item
from character import Enemy

#Setup Characters

dave = Enemy('Dave', 'A smelly zombie')
dave.set_conversation('urrrrgghhh....brraaaaaiiinnssss')
dave.set_weakness('milk')

#Set up rooms
kitchen = Room("Kitchen")
kitchen.set_description("A dark and dirty room buzzing with flies.")
#kitchen.describe()

diningHall = Room("Dining Hall")
diningHall.set_description("A large room with ornate fixtures and fittings")
diningHall.set_character(dave)

ballroom = Room("Ballroom")
ballroom.set_description("A vast room with a shiny wooden floor")

kitchen.link_room(diningHall, "south")
diningHall.link_room(ballroom, "west")
diningHall.link_room(kitchen, "north")
ballroom.link_room(diningHall, "east")

currentRoom = kitchen

#make some items
torch = Item("Torch")
torch.set_description("A battered old torch")

matches = Item("Matches")
matches.set_description("A half  used box of matches")




while True:
    print("\n")
    currentRoom.get_details()

    inhabitant = currentRoom.get_character()
    if inhabitant is not None:
        inhabitant.describe()
        inhabitant.talk()


    command = input("> ")
    if command in ['north', 'south', 'east', 'west']:
        currentRoom = currentRoom.move(command)
    else:
        print("something else")