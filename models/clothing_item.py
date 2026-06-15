# This file contains the definition of the class 'ClothingItem'
# We would be creating an object having the same attributes for each clothing item that the user inputs

from uuid import uuid4


class ClothingItem:
    def __init__(self, id, name, type, category, colour, worn_date_list, wash_date_list):
        if id:
            self.id = id
        else:
            self.id = uuid4()
        self.name = name
        self.type = type
        self.category = category
        self.colour = colour
        if worn_date_list:
            self.worn_date_list = worn_date_list
        else:
            self.worn_date_list = []
        if wash_date_list:
            self.wash_date_list = wash_date_list
        else:
            self.wash_date_list = []

