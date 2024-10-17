import allure
import requests
import src.data

@allure.step('Отправка POST запроса на создание курьера')
def create_courier(data):
    return requests.post(src.data.create_courier_url, json=data)

@allure.step('Отправка DELETE запроса на удаление курьера')
def delete_courier(courier_id):
    return requests.delete(f"{src.data.delete_courier_url}{courier_id}")

@allure.step('Отправка POST запроса на логин курьера')
def login_courier(data):
    return requests.post(src.data.login_courier_url, json=data)

@allure.step('Отправка POST запроса на создание заказа')
def create_order(data):
    return requests.post(src.data.create_order_url, json=data)

@allure.step('Отправка GET запроса на получение списка заказов')
def get_orders():
    return requests.get(src.data.get_orders_url)