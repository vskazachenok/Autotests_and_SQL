import sender_stand_request
import data

# Василиса Казаченок, 8-я когорта - Финальный проект. Инженер по тестированию плюс
# Функция для позитивной проверки
def positive_assert_create_and_get_order():
    order_track_response = sender_stand_request.post_create_order(data.order_body)
    assert order_track_response.status_code == 201

    created_order = sender_stand_request.get_order(order_track_response.json()["track"])
    assert created_order.status_code == 200


# Тест на получение заказа
def test_create_and_get_order():
    positive_assert_create_and_get_order()
