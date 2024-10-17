import allure
import src.helpers as helpers
import src.data as data
import src.api_requests as api

@allure.suite('Тесты удаления курьера')
class TestDeleteCourier:
    @allure.title('Успешное удаление курьера через ручку /api/v1/courier/:id')
    def test_delete_existing_courier_with_valid_id_in_url_courier_deleted(self, use_created_courier_data_for_deletion):
        login_data = helpers.make_login_data(use_created_courier_data_for_deletion)
        courier_id = api.login_courier(login_data).json()['id']
        delete_courier_response = api.delete_courier(courier_id)
        assert delete_courier_response.status_code == 200
        assert 'ok' in delete_courier_response.json() and delete_courier_response.json()['ok'] is True
    
    @allure.title('Удаление курьера без указания id через ручку /api/v1/courier/:id')
    def test_delete_courier_without_id_in_url_shows_missing_id_error(self):
        courier_id = ''
        delete_courier_response = api.delete_courier(courier_id)
        assert delete_courier_response.status_code == 400
        assert 'message' in delete_courier_response.json()
        assert delete_courier_response.json()['message'] == data.DELETE_WITH_EMPTY_ID_ERROR_MESSAGE
    
    @allure.title('Удаление курьера с указанием несуществующего id через ручку /api/v1/courier/:id')
    def test_delete_courier_twice_shows_incorrect_id_error(self, use_created_courier_data_for_deletion):
        login_data = helpers.make_login_data(use_created_courier_data_for_deletion)
        courier_id = api.login_courier(login_data).json()['id']
        delete_courier_response = api.delete_courier(courier_id)
        assert delete_courier_response.status_code == 200
        
        second_delete_courier_response = api.delete_courier(courier_id)
        assert second_delete_courier_response.status_code == 404
        assert 'message' in second_delete_courier_response.json()
        assert second_delete_courier_response.json()['message'] == data.DELETE_WITH_UNEXISTING_ID_ERROR_MESSAGE
        