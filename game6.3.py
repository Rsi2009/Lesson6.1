from bs4 import BeautifulSoup
import requests
from googletrans import Translator

# Создаём объект переводчика, который будет использоваться в функции перевода.
translator = Translator()


def get_english_words():
    # URL сайта, с которого будет извлекаться случайное английское слово и его определение.
    url = "https://randomword.com/"
    try:
        # Отправляем HTTP-запрос на указанный URL и получаем ответ.
        response = requests.get(url)
        # Создаём объект BeautifulSoup для парсинга HTML-контента.
        soup = BeautifulSoup(response.content, "html.parser")
        # Извлекаем слово, используя id тега div. Удаляем лишние пробелы.
        english_word = soup.find("div", id="random_word").text.strip()
        # Извлекаем определение слова, используя id тега div. Удаляем лишние пробелы.
        word_definition = soup.find("div", id="random_word_definition").text.strip()
        # Возвращаем словарь с английским словом и его определением.
        return {
            "english_word": english_word,
            "word_definition": word_definition
        }
    except Exception as e:
        # Печатаем сообщение об ошибке и возвращаем None.
        print(f"Произошла ошибка: {e}")
        return None


def translate_text(text, lang='ru'):
    # Переводим текст на заданный язык (по умолчанию - русский).
    translation = translator.translate(text, dest=lang)
    return translation.text


def word_game():
    # Приветствие игрока.
    print("Добро пожаловать в игру!")
    while True:
        # Получаем словарь с английским словом и его определением.
        word_dict = get_english_words()
        if not word_dict:
            break  # Прерываем игру, если не удалось получить слово.

        word = word_dict.get("english_word")
        word_definition = word_dict.get("word_definition")

        # Переводим слово и его определение на русский язык.
        translated_word = translate_text(word)
        translated_definition = translate_text(word_definition)

        # Выводим определение слова и запрашиваем ответ у пользователя.
        print(f"Значение слова - {translated_definition}")
        user_input = input("Что это за слово? ")
        if user_input.lower() == translated_word.lower():
            print("Всё верно!")
        else:
            print(f"Ответ неверный, было загадано это слово - {translated_word}")

        # Спрашиваем у пользователя, хочет ли он сыграть ещё раз.
        play_again = input("Хотите сыграть ещё раз? да/нет ")
        if play_again.lower() != "да":
            print("Спасибо за игру!")
            break  # Выход из игры.


word_game()