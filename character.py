class Character():

    # Create a character
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None
        self.heldItems = []

    # Describe this character
    def describe(self):
        print("\nYou can see " + self.name + ", " + self.description)
        

    def set_description(self, char_description):
        self.description(char_description)

    # Set what this character will say when talked to
    def set_conversation(self, conversation):
        self.conversation = conversation

    # Talk to this character
    def talk(self):
        if self.conversation is not None:
            print("[" + self.name + " says]: " + self.conversation)
        else:
            print(self.name + " doesn't want to talk to you")

    # Fight with this character
    def fight(self, combat_item):
        print(self.name + " doesn't want to fight with you")
        return True

    #def set_items(self, item_name):
    #    self.heldItems(item_name)

    def get_items(self):
            print(self.heldItems)


class Enemy(Character):
    def __init__(self, char_name, char_description):

        super().__init__(char_name, char_description)
        self.weakness = None

    def fight(self, combat_item):
        if combat_item == self.weakness:
            print("You fend " + self.name + " off with the " + combat_item)
            return True
        else:
            #print(self.name + " crushes you, puny adventurer!")
            return False

    def set_weakness(self, item_weakness):
        self.weakness = item_weakness

    def get_weakness(self):
        return self.weakness

    def steal(self):
        print("you steal from " + self.name)


class Friend(Character):

    def __init__(self, char_name, char_description):

        super().__init__(char_name, char_description)
        self.feeling = None

    def hug(self):
        print(self.name + " hugs you back!")
