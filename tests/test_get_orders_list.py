import allure
import src.api_requests as api

@allure.suite('Тесты получения списка заказов')
class TestGetOrders:
    @allure.title('Успешное получения списка всех заказов с ручкой /api/v1/orders')
    def test_get_orders_shows_list_of_all_orders(self):
        response = api.get_orders()
        assert response.status_code == 200
        assert 'orders' in response.json()