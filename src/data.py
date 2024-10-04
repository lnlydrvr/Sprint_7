# URL сервиса "Яндекс Самокат"
service_url = 'https://qa-scooter.praktikum-services.ru'

# URLы API для функциональности курьера
create_courier_url = service_url + '/api/v1/courier'
login_courier_url = service_url + '/api/v1/courier/login'
delete_courier_url = service_url + '/api/v1/courier/'

# Локаторы для функциональности курьера
CREATE_COURIER_DUPLICATION_ERROR_MESSAGE = 'Этот логин уже используется'
CREATE_COURIER_EMPTY_FIELD_ERROR_MESSAGE = 'Недостаточно данных для создания учетной записи'
LOGIN_WITH_INCORRECT_DATA_ERROR_MESSAGE = 'Учетная запись не найдена'
LOGIN_WITH_EMPTY_FIELD_ERROR_MESSAGE = 'Недостаточно данных для входа'

# URLы API для функциональности заказов
create_order_url = service_url + '/api/v1/orders'
get_orders_url = service_url + '/api/v1/orders'

# Данные для тестовых заказов
ORDER_INFO_NO_COLOR = {
    "firstName": "Naruto",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2024-10-05",
    "comment": "Saske, come back to Konoha",
    "color": []
    }

ORDER_INFO_COLOR_BLACK = {
    "firstName": "Naruto",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2024-10-05",
    "comment": "Saske, come back to Konoha",
    "color": ["BLACK"]
    }

ORDER_INFO_COLOR_GREY = {
    "firstName": "Naruto",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2024-10-05",
    "comment": "Saske, come back to Konoha",
    "color": ["GRAY"]
    }

ORDER_INFO_COLOR_BLACK_AND_GREY = {
    "firstName": "Naruto",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2024-10-05",
    "comment": "Saske, come back to Konoha",
    "color": ["BLACK", "GREY"]
    }