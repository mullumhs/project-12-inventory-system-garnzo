"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                                LAB 2
-----------------------------------------------------------------------------------------------
- File Name: lab2.py
- Teacher: David Steedman
- Class: Software Engineering
- Description: Extend the functionality developed in Lab 1 by creating an InventoryManager class 
               that acts as a facade for managing an inventory of items. Demonstrate the use of 
               encapsulation and the facade design pattern through practical examples.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Step 1: Import the Item class from lab1.py
from lab1 import Item

# Step 2: Define the InventoryManager class as a facade to handle the inventory operations.
# It should include methods to add, remove, update, and display items in the inventory.
class InventoryManager:
    
    def __init__(self):
        self._items = []

    def add_item(self, item_name, price, qty):
        for item in self._items:
            if item_name == item.get_item():
                raise ValueError("Item already in list")
        self._items.append(item_name)

    def remove_item(self, item_name):
        for item in self._items:
            if item_name == item.get_item():
                self._items.remove(item_name)          
        raise ValueError("Item Doesn't Exist")

    def update_item(self, item_name, new_item_name):
        for item in self._items:
            if item_name == item.get_item():
                item.set_item(new_item_name)       
        raise ValueError("Item Doesn't Exist")
        
    def update_price(self, item_name, price, new_price):
        for item in self._items:
            if item_name == item.get_item():
                item.set_price(new_price)
    def update_qty(self, item_name, new_qty):
        for item in self._items:
            if item_name == item.get_item():
                item.set_qty(new_qty)
        raise ValueError("Error")

    def display_items(self):
        for item in self._items:
            return(self._items)
    
    def find_item(self, item_name):
        for item in self._items:
            if item_name == item.get_item():
                return(f"Item Found {item}")
                

# Step 2: Create instances of the Item class and InventoryManager, then demonstrate their usage.
# E.g. add items to the inventory, remove items, update items, and display the inventory.

inv = InventoryManager()
inv.add_item("Johnny Depp Cigars 3 Pack", "$150.00", 50)

