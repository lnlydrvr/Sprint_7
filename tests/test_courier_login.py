import allure
import src.helpers as helpers
import src.data as data
import src.api_requests as api

@allure.suite('Тесты логина курьера')
class TestLoginCourier:
    @allure.title('Успешная авторизация курьера через ручку /api/v1/courier/login')
    def test_courier_login_with_valid_data_courier_logged_in(self, use_created_courier_data):
        login_data = helpers.make_login_data(use_created_courier_data)
        login_response = api.login_courier(login_data)
        assert login_response.status_code == 200
        assert 'id' in login_response.json()

    @allure.title('Авторизация курьера с неверным логином через ручку /api/v1/courier/login')
    def test_courier_login_with_incorrect_login_courier_not_logged_in(self, use_created_courier_data):
        login_data = helpers.make_login_data(use_created_courier_data)
        new_data = helpers.generate_new_courier_data()
        login_data['login'] = new_data['login']
        login_response = api.login_courier(login_data)
        assert login_response.status_code == 404
        assert 'message' in login_response.json()
        assert login_response.json()['message'] == data.LOGIN_WITH_INCORRECT_DATA_ERROR_MESSAGE

    @allure.title('Авторизация курьера с неверным паролем через ручку /api/v1/courier/login')
    def test_courier_login_with_incorrect_password_courier_not_logged_in(self, use_created_courier_data):
        login_data = helpers.make_login_data(use_created_courier_data)
        new_data = helpers.generate_new_courier_data()
        login_data['password'] = new_data['password']
        login_response = api.login_courier(login_data)
        assert login_response.status_code == 404
        assert 'message' in login_response.json()
        assert login_response.json()['message'] == data.LOGIN_WITH_INCORRECT_DATA_ERROR_MESSAGE

    @allure.title('Авторизация курьера с пустым логином через ручку /api/v1/courier/login')
    def test_courier_login_with_empty_login_courier_not_logged_in(self, use_created_courier_data):
        login_data = helpers.make_login_data(use_created_courier_data)
        login_data['login'] = ''
        login_response = api.login_courier(login_data)
        assert login_response.status_code == 400
        assert 'message' in login_response.json()
        assert login_response.json()['message'] == data.LOGIN_WITH_EMPTY_FIELD_ERROR_MESSAGE

    @allure.title('Авторизация курьера с пустым паролем через ручку /api/v1/courier/login')
    def test_courier_login_with_empty_password_courier_not_logged_in(self, use_created_courier_data):
        login_data = helpers.make_login_data(use_created_courier_data)
        login_data['password'] = ''
        login_response = api.login_courier(login_data)
        assert login_response.status_code == 400
        assert 'message' in login_response.json()
        assert login_response.json()['message'] == data.LOGIN_WITH_EMPTY_FIELD_ERROR_MESSAGE