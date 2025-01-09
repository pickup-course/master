# test_composite.py
# BDD-тестирование для паттерна Компоновщик

import pytest
from pytest_bdd import scenario, given, when, then
from composite import SingularProduct, ProductPack

@pytest.fixture
def product():
    return SingularProduct("Сигарета 'Беломорканал'")

@pytest.fixture
def pack():
    return ProductPack("Пачка сигарет")

@scenario('composite.feature', 'Упаковка пачки')
def test_composite():
    pass

@given('одна сигарета')
def product_fixture(product):
    return product

@given('пачка сигарет')
def pack_fixture(pack):
    return pack

@when('сигарета кладется в пачку')
def cig2pack(product, pack):
    pack.add(product)

@then('сигарета отображается в составе данной пачки')
def check_pack(pack):
    assert pack.get_desc() == "В пачке: Пачка сигарет, находятся: Сигарета 'Беломорканал'"
