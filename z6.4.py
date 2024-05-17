from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def list_paragraphs(browser):
    paragraphs = browser.find_elements(By.TAG_NAME, 'p')
    for i, paragraph in enumerate(paragraphs):
        print(f"Параграф {i + 1}: {paragraph.text}")
        if i % 5 == 4:  # После каждых 5 параграфов спрашиваем у пользователя, продолжить ли
            cont = input("Хотите продолжить листать параграфы? (да/нет): ")
            if cont.lower() != 'да':
                break

def choose_link(browser):
    links = browser.find_elements(By.CSS_SELECTOR, 'a[href^="/wiki/"]')
    for i, link in enumerate(links):
        print(f"Ссылка {i + 1}: {link.text} ({link.get_attribute('href')})")
        if i % 5 == 4:  # После каждых 5 ссылок спрашиваем у пользователя, продолжить ли
            cont = input("Хотите продолжить просматривать ссылки? (да/нет): ")
            if cont.lower() != 'да':
                break

    if links:
        choice = int(input(f"Выберите номер ссылки (1-{len(links)}): "))
        if 1 <= choice <= len(links):
            browser.get(links[choice - 1].get_attribute('href'))
        else:
            print("Некорректный выбор.")
    else:
        print("Нет доступных ссылок.")

def main():
    query = input("Введите запрос: ")
    browser = webdriver.Firefox()
    browser.get(f"https://ru.wikipedia.org/wiki/{query}")
    print(f"По Вашему запросу Вы перешли на страницу wikipedia {query}")

    while True:
        print("Выберите действие:")
        print("1. Листать параграфы текущей статьи")
        print("2. Перейти на одну из связанных страниц")
        print("3. Выйти")

        choice = input("Введите номер действия: ")

        if choice == '1':
            list_paragraphs(browser)
        elif choice == '2':
            choose_link(browser)
            while True:
                print("Выберите действие на новой странице:")
                print("1. Листать параграфы статьи")
                print("2. Перейти на одну из внутренних статей")
                print("3. Выйти к предыдущему меню")

                sub_choice = input("Введите номер действия: ")

                if sub_choice == '1':
                    list_paragraphs(browser)
                elif sub_choice == '2':
                    choose_link(browser)
                elif sub_choice == '3':
                    break
                else:
                    print("Некорректный выбор. Попробуйте снова.")
        elif choice == '3':
            break
        else:
            print("Некорректный выбор. Попробуйте снова.")

    browser.quit()

if __name__ == "__main__":
    main()