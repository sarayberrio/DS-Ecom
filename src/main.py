from ecommercecompany import ECommerceCompany
from ordermanagement import OrderManagement
from paymentprocessing import PaymentProcessing
from inventory import Inventory
from gateway import Gateway


def main():
    order_management = OrderManagement()

    payment_processing = PaymentProcessing()

    inventory = Inventory()

    gateway = Gateway(order_management, payment_processing, inventory)

    e_commerce_company = ECommerceCompany(gateway)

    e_commerce_company.main()


if __name__ == '__main__':
    main()
