import requests
from bs4 import BeautifulSoup
from googletrans import Translator


# Создаём функцию, которая будет получать информацию
def get_english_words():
    url = "https://randomword.com/"
    try:
        response = requests.get(url)

        # Создаём объект Soup
        soup = BeautifulSoup(response.content, "html.parser")
        # Получаем слово. text.strip удаляет все пробелы из результата
        english_word = soup.find("div", id="random_word").text.strip()
        # Получаем описание слова
        word_definition = soup.find("div", id="random_word_definition").text.strip()

        # Возвращаем словарь с оригинальным словом и его описанием
        return {
            "english_word": english_word,
            "word_definition": word_definition
        }
    except:
        print("Произошла ошибка при получении слова и его описания")


# Функция для перевода слова и его описания на русский язык
def translate_to_russian(text):
    translator = Translator()
    result = translator.translate(text, src='en', dest='ru')
    return result.text


# Создаём функцию, которая будет проводить игру
def word_game():
    print("Добро пожаловать в игру!")
    while True:
        # Получаем случайное английское слово и его определение
        word_dict = get_english_words()
        if not word_dict:
            break
        english_word = word_dict.get("english_word")
        english_definition = word_dict.get("word_definition")

        # Переводим слово и его описание на русский
        russian_word = translate_to_russian(english_word)
        russian_definition = translate_to_russian(english_definition)

        # Начинаем игру
        print(f"Значение слова - {russian_definition}")
        user = input("Что это за слово? (Введите перевод на русский) ")
        if user.lower() == russian_word.lower():
            print("Все верно!")
        else:
            print(f"Ответ неверный, правильный ответ - {russian_word}")

        # Возможность закончить игру
        play_again = input("Хотите сыграть еще раз? y/n ")
        if play_again.lower() != "y":
            print("Спасибо за игру!")
            break


# Запускаем игру
word_game()
