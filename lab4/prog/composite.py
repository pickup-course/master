# composite.py
# Реализует структурный паттерн - Компоновщик

class Product:
    def get_desc(self):
        pass

class SingularProduct(Product):
    def __init__(self, name):
        self.name = name

    def get_desc(self):
        return self.name

class ProductPack(Product):
    def __init__(self, name):
        self.name = name
        self._components = []

    def add(self, product: Product):
        self._components.append(product)

    def get_desc(self):
        descs = [component.get_desc() for component in self._components]
        return f"В пачке: {self.name}, находятся: {', '.join(descs)}"
