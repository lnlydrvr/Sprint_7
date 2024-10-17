import pytest
import src.helpers as helpers

@pytest.fixture
def use_courier_data():
    courier_data = helpers.create_new_courier()
    yield courier_data
    helpers.delete_courier(courier_data)
    
@pytest.fixture
def use_created_courier_data():
    courier_data = helpers.create_new_courier(register=True)
    yield courier_data
    helpers.delete_courier(courier_data)

@pytest.fixture
def use_created_courier_data_for_deletion():
    courier_data = helpers.create_new_courier(register=True)
    yield courier_data