class Item():
    def __init__(self, itemName):
        self.name = itemName
        self.description = None

    def set_description(self, itemDescription):
        self.description = itemDescription

    def get_description(self):
        return self.description

    def set_name(self, itemName):
        self.name = itemName

    def get_name(self):
        return self.name

    def describe(self):
        print(self.description)
