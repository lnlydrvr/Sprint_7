import pytest
import allure
import src.data as data
import src.api_requests as api
import src.helpers as helpers

@allure.suite('Тесты ручки на создание курьера')
class TestCreateCourier:
    @allure.title('Создание курьера через ручку /api/v1/courier')
    def test_create_new_courier_with_valid_data_courier_created(self, use_courier_data):
        create_courier_response = api.create_courier(use_courier_data)
        assert create_courier_response.status_code == 201
        assert 'ok' in create_courier_response.json() and create_courier_response.json()['ok'] is True

    @allure.title('Создание курьера с пустыми обязательными полями через ручку /api/v1/courier')
    @pytest.mark.parametrize('empty_fields',
        [
            helpers.generate_new_courier_data(empty_field='login'),
            helpers.generate_new_courier_data(empty_field='password')
        ])
    def test_create_new_courier_with_empty_login_or_password_courier_not_created(self, empty_fields):
        create_courier_response = api.create_courier(empty_fields)
        assert create_courier_response.status_code == 400
        assert 'message' in create_courier_response.json()
        assert create_courier_response.json()['message'] == data.CREATE_COURIER_EMPTY_FIELD_ERROR_MESSAGE

    @allure.title('Создание курьера с пустым именем через ручку /api/v1/courier')
    def test_create_courier_with_empty_name_courier_created(self, use_courier_data):
        use_courier_data['firstName'] = ''
        create_courier_response = api.create_courier(use_courier_data)
        assert create_courier_response.status_code == 201
        assert 'ok' in create_courier_response.json() and create_courier_response.json()['ok'] is True
    
    @allure.title('Создание двух одинаковых курьеров через ручку /api/v1/courier')
    def test_create_two_identical_couriers_second_courier_not_created(self, use_courier_data):
        create_first_courier_response = api.create_courier(use_courier_data)
        assert create_first_courier_response.status_code == 201

        create_second_courier_response = api.create_courier(use_courier_data)
        assert create_second_courier_response.status_code == 409
        assert 'message' in create_second_courier_response.json()
        assert create_second_courier_response.json()['message'] == data.CREATE_COURIER_DUPLICATION_ERROR_MESSAGE