#test_field.py

import pytest
from pytest_bdd import scenario, given, when, then
from field import field

@pytest.fixture
def test_data():
    return [
        {"имя": "Анна", "возраст": 30, "email": "anna@mail.ru"},
        {"имя": "Борис", "возраст": 25, "email": None},
        {"имя": "Владимир", "возраст": None, "email": "vladimir@gmail.com"},
    ]

@pytest.fixture
def context():
    return {}

@scenario('field.feature', 'Выборка по одному полю из массива словарей')
def test_single_field():
    pass

@given('массив словарей')
def data(context, test_data):
    context['data'] = test_data

@when('происходит выборка по имени')
def names(context):
    context['result'] = list(field(context['data'], "имя"))

@then('выводится массив имен')
def check_names(context):
    check = ["Анна", "Борис", "Владимир"]
    assert context['result'] == check, f"Ожидалось {check}, получено {context['result']}"

@scenario('field.feature', 'Выборка по нескольким полям из массива словарей')
def test_multiple_fields():
    pass

@given('массив словарей')
def data(context, test_data):
    context['data'] = test_data

@when('происходит выборка по полям "имя" и "возраст"')
def names_ages(context):
    context['result'] = list(field(context['data'], "имя", "возраст"))

@then('выводится массив полей "имя" и "возраст"')
def check_names_ages(context):
    check = [
        {"имя": "Анна", "возраст": 30},
        {"имя": "Борис", "возраст": 25},
        {"имя": "Владимир"}
    ]
    assert context['result'] == check, f"Ожидалось {check}, получено {context['result']}"

@scenario('field.feature', 'Пропуск полей "None"')
def test_field_with_none():
    pass

@given('массив словарей')
def data(context, test_data):
    context['data'] = test_data

@when('происходит выборка по полю "email"')
def emails(context):
    context['result'] = list(field(context['data'], "email"))

@then('выводится массив полей email без значений "None"')
def check_emails(context):
    check = ["anna@mail.ru", "vladimir@gmail.com"]
    assert context['result'] == check, f"Ожидалось {check}, получено {context['result']}"
