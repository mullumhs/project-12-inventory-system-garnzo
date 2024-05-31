"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                                LAB 1
-----------------------------------------------------------------------------------------------
- File Name: lab1.py
- Teacher: David Steedman
- Class: Software Engineering
- Description: Create a class named Item that represents a generic item in an inventory system.
               Implement encapsulation using private attributes and public getters and setters.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Step 1: Define the Item class with initialisation that uses setters for name, price, and quantity.
# Instead of directly setting private attributes in the __init__ method, use the class's own setters
# We will define the setters in later steps to add validation to the setting of these attributes.
class Item:
    
    def __init__(self, Item, price, qty):
        self._Item = Item
        self._price = price
        self._qty = qty

    def get_item(self):
        return self._Item
        return self._Item
        return self._qty

    def get_price(self):
        return self._price

    def get_qty(self):
        return self._qty
    
    def set_Item(self, new_item):
        pass

    def set_price(self, new_price):
        if new_price < 0:
            raise ValueError("New Price can't be lower than 0")
        else:
            self._price = new_price
            
    def set_qty(self, new_qty):
        if new_qty < 0:
            raise ValueError("Quantity can't be lower than 0")
        else:
            self._qty = new_qty


# Step 2: Implement a getter for the name attribute.
# This method should simply return the value of the private _name attribute.





# Step 3: Implement a setter for the name attribute.
# This method should check if the provided value is a string before setting the _name attribute.
# If the value is not a string, it should raise a ValueError.





# Step 4: Implement a getter for the price attribute.
# This method should return the price formatted as a string with two decimal places.





# Step 5: Implement a setter for the price attribute.
# This method should check if the provided value is a non-negative number before setting the _price attribute.
# If the value is negative, it should raise a ValueError.





# Step 6: Implement a getter for the quantity attribute.
# This method should simply return the value of the private _quantity attribute.





# Step 7: Implement a setter for the quantity attribute.
# This method should check if the provided value is a non-negative integer before setting the _quantity attribute.
# If the value is negative, it should raise a ValueError.





# Step 8: Create instances of the Item class and demonstrate the use of getters and setters.
# For example, create a new Item and attempt to set its attributes with both valid and invalid values.
# Print the outputs using the getters to show how the data is managed internally.




