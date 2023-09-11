import configuration
import requests
import data


def post_create_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.ORDERS_PATH,
                         json=body,
                         headers=data.headers)


def get_order(order_id):
    return requests.get(configuration.URL_SERVICE + configuration.ORDERS_PATH, params={"t": order_id})


response = post_create_order(data.order_body)
print(response.status_code)
print(response.json())
