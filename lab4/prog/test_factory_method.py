# test_factory_method.py
# TDD-тестирование для паттерна фабричный метод

import unittest
from factory_method import BulletFactory, CigaretteFactory

class TestFactoryMethod(unittest.TestCase):
    def test_factory_method(self):
        bullet_factory = BulletFactory()
        cigarette_factory = CigaretteFactory()

        bullet = bullet_factory.create_product()
        self.assertEqual(bullet.get_desc(), "Произведен патрон")

        cigarette = cigarette_factory.create_product()
        self.assertEqual(cigarette.get_desc(), "Произведена сигарета")

if __name__ == "__main__":
    unittest.main()
