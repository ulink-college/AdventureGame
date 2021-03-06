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



#Create some sort of inventory for holding items
class Inventory():
    def __init__(self):
        self.contents = {}

    def add(self, item, qty = 1):
        name = str(item)
        self.contents[name] = qty

    def describe(self):
        for i in  self.contents.keys():
            print(i, end = ", ")
