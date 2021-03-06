class Room():
    #create a room
    def __init__(self, room_name):         #defines constructor method - tells python to create an object of this class
        self.name = room_name        #define some attributes
        self.description = None
        self.linked_rooms = {}
        self.character = None
        self.stuff = {}

    #Describe the room
    def set_description(self, room_description):
        self.description = room_description

    def get_description(self):
        return self.description

    def set_name(self, room_name):
        self.name = room_name

    def get_name(self):
        return self.name

    def describe(self):
        print(self.description)

    def link_room(self, room_to_link, direction):
        self.linked_rooms[direction] = room_to_link
        #print(self.name + " linked rooms :" + repr(self.linked_rooms))

    def room_items(self, thing_in_room, qty=1):
        self.stuff[thing_in_room] = qty
        #print(self.name + " linked rooms :" + repr(self.linked_rooms))

    def get_stuff(self):
        print("You can take:")
        for i in self.stuff:
            print("   " + i + " x " + str(self.stuff[i]))


    def get_details(self):
        print(self.name)
        print("------------")
        print(self.description)
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print("The " + room.get_name() + " is " + direction)

    def move(self, direction):
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("you can't go that way")
            return self

    def set_character(self,character_name):
        self.character = character_name

    def get_character(self):
        return self.character
