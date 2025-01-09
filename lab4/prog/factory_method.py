# factory_method.py
# Реализует порождающий шаблон - Фабричный метод

from abc import ABC, abstractmethod

class Product(ABC):
    @abstractmethod
    def get_desc(self):
        pass

class Bullet(Product):
    def get_desc(self):
        return "Произведен патрон"

class Cigarette(Product):
    def get_desc(self):
        return "Произведена сигарета"

class Factory(ABC):
    @abstractmethod
    def create_product(self):
        pass

class BulletFactory(Factory):
    def create_product(self):
        return Bullet()

class CigaretteFactory(Factory):
    def create_product(self):
        return Cigarette()
