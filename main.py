from bs4 import BeautifulSoup
import requests
from googletrans import Translator

translator = Translator()


def get_english_words():
    url = "https://randomword.com/"
    try:
        response = requests.get(url)

        # Создаём объект Soup
        soup = BeautifulSoup(response.content, "html.parser")
        # Получаем слово. text.strip удаляет все пробелы из результата
        english_words = soup.find("div", id="random_word").text.strip()
        # Получаем описание слова
        word_definition = soup.find("div", id="random_word_definition").text.strip()
        # Чтобы программа возвращала словарь
        return {
            "english_words": english_words,
            "word_definition": word_definition
        }
    # Функция, которая сообщит об ошибке, но не остановит программу
    except:
        print("Произошла ошибка")

### 3. Функция для перевода текста
def translate_text(text, lang='ru'):
    translator = Translator()
    translation = translator.translate(text, dest=lang)
    return translation.text
# Создаём функцию, которая будет делать саму игру
def word_game():
    print("Добро пожаловать в игру")
    while True:
        # Создаём функцию, чтобы использовать результат функции-словаря
        word_dict = get_english_words()
        word = word_dict.get("english_words")
        word_definition = word_dict.get("word_definition")

        translated_word = translate_text(word)
        translated_definition = translate_text(word_definition)

        # Начинаем игру
        print(f"Значение слова - {translated_definition}")
        user = input("Что это за слово? ")
        if user == translated_word:
            print("Все верно!")
        else:
            print(f"Ответ неверный, было загадано это слово - {translated_word}")

        # Создаём возможность закончить игру
        play_again = input("Хотите сыграть еще раз? да/нет ")
        if play_again != "да":
            print("Спасибо за игру!")
            break


word_game()
