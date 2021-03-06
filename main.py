from room import Room
from item import Item
from character import Character, Enemy, Friend

#Setup Characters
dave = Enemy('Dave', 'A smelly zombie')
dave.set_conversation('urrrrgghhh....brraaaaaiiinnssss')
dave.set_weakness('milk')
#dave.set_items('meat')

bill = Friend('Bill', 'A small black kitten')
bill.set_conversation('Meow')

#Set up rooms
kitchen = Room("Kitchen")
kitchen.set_description("A dark and dirty room buzzing with flies.")
kitchen.set_character(bill)

diningHall = Room("Dining Hall")
diningHall.set_description("A large room with ornate fixtures and fittings")
diningHall.set_character(dave)

ballroom = Room("Ballroom")
ballroom.set_description("A vast room with a shiny wooden floor")

kitchen.link_room(diningHall, "south")
diningHall.link_room(ballroom, "west")
diningHall.link_room(kitchen, "north")
ballroom.link_room(diningHall, "east")

kitchen.room_items("Knife", 2)

currentRoom = kitchen

#make some items
torch = Item("Torch")
torch.set_description("A battered old torch")

matches = Item("Matches")
matches.set_description("A half  used box of matches")

dead = False
while dead == False:
    print("\n")
    currentRoom.get_details()
    currentRoom.get_stuff()

    inhabitant = currentRoom.get_character()
    if inhabitant is not None:
        inhabitant.describe()
        #inhabitant.talk()


    command = input("> ")
    if command in ['north', 'south', 'east', 'west']:
        currentRoom = currentRoom.move(command)
    elif command == "talk":
        inhabitant.talk()
    elif command == "fight":
        if inhabitant == None or isinstance(inhabitant, Friend):
            print("You swing wildly at thin air. There is no one there")
        else:
            fightWith = input("What will you fight with? \n")
            if inhabitant.fight(fightWith)  == True:
                print("You won")
                currentRoom.set_character(None)
            else:
                print("Dead")
                input("Press a key to end")
                dead = True
    elif command == "hug":
        if isinstance(inhabitant, Enemy):
            print("I wouldn't do that...")
        else:
            inhabitant.hug()

        
