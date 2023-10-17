import json


class Inventory:
    """A class that manages inventory.

    Attributes:
        inventory_data: A dictionary of inventory data.

    Product  JSON
    {
        "id": int,
        "name": string,
        "price": float,
        "quantity": int
    }
    """

    def __init__(self):
        # read from json file
        data = open('temp_db/inventory.json', 'r')
        self.inventory_data = json.load(data)

    def _save_inventory(self):
        """Saves the inventory data to a json file."""
        with open('temp_db/inventory.json', 'w') as file:
            json.dump(self.inventory_data, file)

    def get_products(self):
        """Returns a list of products."""
        return self.inventory_data['products']

    def get_product(self, product_id):
        """Returns a product."""
        for product in self.inventory_data['products']:
            if product['id'] == product_id:
                return product
        return None

    def create_product(self, product):
        """Creates a product."""
        # check if product already exists
        for existing_product in self.inventory_data['products']:
            if existing_product['id'] == product['id']:
                return "Product already exists."

        # check if product structure is valid
        if 'id' not in product or 'name' not in product or \
                'price' not in product or 'quantity' not in product:
            return "Invalid product structure."

        self.inventory_data['products'].append(product)
        self._save_inventory()
        return "Product created."

    def update_product(self, product_id, product):
        """Updates a product."""
        for i, producti in enumerate(self.inventory_data['products']):
            if producti['id'] == product_id:
                self.inventory_data['products'][i] = product
                self._save_inventory()
                return "Product updated."
        return "Product not found."

    def delete_product(self, product_id):
        """Deletes a product."""
        for i, product in enumerate(self.inventory_data['products']):
            if product['id'] == product_id:
                del self.inventory_data['products'][i]
                self._save_inventory()
                return "Product deleted."
        return "Product not found."
