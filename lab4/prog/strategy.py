# strategy.py
# Реализует поведеденческий шаблон - стратегия

from abc import ABC, abstractmethod

class DeliveryStrategy(ABC):
    @abstractmethod
    def deliver(self, order):
        pass

class StandardDelivery(DeliveryStrategy):
    def deliver(self, order):
        return f"Доставляю {order} стандартной доставкой."

class ExpressDelivery(DeliveryStrategy):
    def deliver(self, order):
        return f"Доставляю {order} экспресс-доставкой."

class Order:
    def __init__(self, delivery_strategy: DeliveryStrategy):
        self.delivery_strategy = delivery_strategy

    def set_delivery_strategy(self, delivery_strategy: DeliveryStrategy):
        self.delivery_strategy = delivery_strategy

    def deliver_order(self, order):
        return self.delivery_strategy.deliver(order)
