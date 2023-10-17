class Gateway:
    """A class that manages APIs.

    Attributes:
        order_management: An OrderManagement object.
        payment_processing: A PaymentProcessing object.
        inventory: An Inventory object.
    """

    def __init__(self, order_management, payment_processing, inventory):
        self.order_management = order_management
        self.payment_processing = payment_processing
        self.inventory = inventory

    def create_api(self, app):
        """Creates an API.
        param app: A FastAPI app.
        """
        @app.get('/products')
        def get_products():
            """Returns a list of products."""
            return self.inventory.get_products()

        @app.get('/products/{product_id}')
        def get_product(product_id: int):
            """Returns a product."""
            product = self.inventory.get_product(product_id)
            if product is None:
                return {'message': 'Product not found.'}
            return product

        @app.post('/products')
        def create_product(product: dict):
            """Creates a product."""
            result = self.inventory.create_product(product)
            return {'message': result}

        @app.put('/products/{product_id}')
        def update_product(product_id: int, product: dict):
            """Updates a product."""
            result = self.inventory.update_product(product_id, product)
            return {'message': result}

        @app.delete('/products/{product_id}')
        def delete_product(product_id: int):
            """Deletes a product."""
            result = self.inventory.delete_product(product_id)
            return {'message': result}

        @app.get('/orders')
        def get_orders():
            """Returns a list of orders."""
            return self.order_management.get_orders()

        @app.get('/orders/{order_id}')
        def get_order(order_id: int):
            """Returns an order."""
            order = self.order_management.get_order(order_id)
            if order is None:
                return {'message': 'Order not found.'}
            return order

        @app.post('/orders')
        def create_order(order: dict):
            """Creates an order."""
            result = self.order_management.create_order(order)
            return {'message': result}

        @app.put('/orders/{order_id}')
        def update_order(order_id: int, order: dict):
            """Updates an order."""
            result = self.order_management.update_order(order_id, order)
            return {'message': result}

        @app.delete('/orders/{order_id}')
        def delete_order(order_id: int):
            """Deletes an order."""
            result = self.order_management.delete_order(order_id)
            return {'message': result}

        @app.get('/payments')
        def get_payments():
            """Returns a list of payments."""
            return self.payment_processing.get_payments()

        @app.get('/payments/{payment_id}')
        def get_payment(payment_id: int):
            """Returns a payment."""
            payment = self.payment_processing.get_payment(payment_id)
            if payment is None:
                return {'message': 'Payment not found.'}
            return payment

        @app.post('/payments')
        def create_payment(payment: dict):
            """Creates a payment."""
            result = self.payment_processing.create_payment(payment)
            return {'message': result}

        @app.put('/payments/{payment_id}')
        def update_payment(payment_id: int, payment: dict):
            """Updates a payment."""
            result = self.payment_processing.update_payment(
                payment_id, payment)
            return {'message': result}

        @app.delete('/payments/{payment_id}')
        def delete_payment(payment_id: int):
            """Deletes a payment."""
            result = self.payment_processing.delete_payment(payment_id)
            return {'message': result}
