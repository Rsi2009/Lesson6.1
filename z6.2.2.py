# Задание 2: Параметры запроса
#
# Используйте API, который позволяет фильтрацию данных через URL-параметры (например, https://jsonplaceholder.typicode.com/posts).
#
# Отправьте GET-запрос с параметром userId, равным 1.
#
# Распечатайте полученные записи.

import requests
import pprint

response = requests.get('https://jsonplaceholder.typicode.com/posts', params={'userId': 1})

response_json = response.json()

pprint.pprint(response.json())
