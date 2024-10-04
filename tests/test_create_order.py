import pytest
import allure
import src.api_requests as api
import src.data as data

@allure.suite('Тесты ручки на создание заказа')
class TestCreateOrders:
    @allure.title('Успешное создание заказа с применением необходимой информации о заказе и ручкой /api/v1/orders')
    @pytest.mark.parametrize('order_info',
        [
            data.ORDER_INFO_NO_COLOR,
            data.ORDER_INFO_COLOR_BLACK,
            data.ORDER_INFO_COLOR_GREY,
            data.ORDER_INFO_COLOR_BLACK_AND_GREY
        ])
    def test_order_creation_with_valid_info_order_created(self, order_info):
        response = api.create_order(order_info)
        assert response.status_code == 201
        assert 'track' in response.json()