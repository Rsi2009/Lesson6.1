# Импортируйте библиотеку requests.
#
# Отправьте GET-запрос к открытому API (например, https://api.github.com) с параметром для поиска репозиториев с кодом html.
#
# Распечатайте статус-код ответа.
#
# Распечатайте содержимое ответа в формате JSON.

import requests

response = requests.get('https://api.github.com/repositories', params={'q': 'html'})
print(response.status_code)
print(response.json())
