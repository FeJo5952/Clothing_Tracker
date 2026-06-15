# The file contains the definition of the Wardrobe Manager class
# The class would define basic functions which can be performed on the constructed objects of the class and objects created by the ClothingItem class also

import os
import json
from models.clothing_item import ClothingItem


class WardrobeManager:
    def __init__(self):
        self.cloth_list = []
        self.load_data()
        
    
    def load_data(self):
        json_path = r"data\clothes.json"
        if not os.path.exists(json_path):
            self.cloth_list = []
            return
        
        with open(json_path,"r") as file:
            data = json.load(file)
        for clothing_item in data:
            id = clothing_item["id"]
            name = clothing_item["name"]
            category = clothing_item["category"]
            type = clothing_item["type"]
            colour = clothing_item["colour"]
            worn_date_list = clothing_item["worn_date_list"]
            wash_date_list = clothing_item["wash_date_list"]

            cloth = ClothingItem(
                id, name, type, category, colour, worn_date_list, wash_date_list
            )

            self.cloth_list.append(cloth)

    def save_data(self):
        pass

    def remove_clothing_item(self):
        pass

    def add_clothing_item(self):
        pass

    def update_clothing_item(self):
        pass

    def list_clothing_items(self):
        pass
    
