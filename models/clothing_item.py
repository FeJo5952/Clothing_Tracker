# This file contains the definition of the class 'ClothingItem'
# We would be creating an object having the same attributes for each clothing item that the user inputs


class ClothingItem:
    def __init__(self, id, name, category, last_washed_date):
        self.id = id
        self.name = name
        self.category = category
        self.wear_count = 0
        self.last_worn_date = None
        self.last_washed_date = last_washed_date
        