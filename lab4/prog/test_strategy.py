# test_strategy.py
# Тестирование паттерна Стратегия с помощью Mock-объектов

import unittest
from unittest.mock import Mock
from strategy import Order, StandardDelivery, ExpressDelivery

class TestStrategy(unittest.TestCase):
    def test_delivery_strategy(self):
        standard_delivery = Mock(spec=StandardDelivery)
        express_delivery = Mock(spec=ExpressDelivery)

        order = Order(standard_delivery)

        order.deliver_order("Заказ #123")

        standard_delivery.deliver.assert_called_with("Заказ #123")

        order.set_delivery_strategy(express_delivery)

        order.deliver_order("Заказ #124")
        express_delivery.deliver.assert_called_with("Заказ #124")

if __name__ == "__main__":
    unittest.main()
