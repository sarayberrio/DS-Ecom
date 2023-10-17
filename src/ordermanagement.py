import json


class OrderManagement:
    """A class that manages orders.

    Attributes:
        order_data: A dictionary of order data.

    order JSON
    {
        "id": int,
        "customer_id": int,
        "products": []int
        "quantity": dict{int: int} # product_id: quantity
        "address": string
        "status": string
    }
    """

    def __init__(self):
        # read from json file
        data = open('temp_db/orders.json', 'r')
        self.order_data = json.load(data)

    def _save_orders(self):
        """Saves the order data to a json file."""
        with open('temp_db/orders.json', 'w') as file:
            json.dump(self.order_data, file)

    def get_orders(self):
        """Returns a list of orders."""
        return self.order_data['orders']

    def get_order(self, order_id):
        """Returns an order."""
        for order in self.order_data['orders']:
            if order['id'] == order_id:
                return order
        return None

    def create_order(self, order, gateway):
        """Creates an order."""
        # check if order already exists
        for existing_order in self.order_data['orders']:
            if existing_order['id'] == order['id']:
                return "Order already exists."

        # check if order structure is valid
        if 'id' not in order or 'customer_id' not in order or \
                'products' not in order or 'quantity' not in order or \
                'address' not in order or 'status' not in order:
            return "Invalid order structure."

        # check if products exist
        for product_id in order['products']:
            product = gateway.inventory.get_product(product_id)
            if product is None:
                return f"Product with id {product_id} does not exist."

        self.order_data['orders'].append(order)
        self._save_orders()
        return "Order created."

    def update_order(self, order_id, order):
        """Updates an order."""
        for i, orderi in enumerate(self.order_data['orders']):
            if orderi['id'] == order_id:
                self.order_data['orders'][i] = order
                self._save_orders()
                return "Order updated."
        return "Order not found."

    def delete_order(self, order_id):
        """Deletes an order."""
        for i, order in enumerate(self.order_data['orders']):
            if order['id'] == order_id:
                del self.order_data['orders'][i]
                self._save_orders()
                return "Order deleted."
        return "Order not found."
