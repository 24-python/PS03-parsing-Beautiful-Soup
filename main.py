from bs4 import BeautifulSoup  # Импортируем библиотеку BeautifulSoup для парсинга HTML
import requests  # Импортируем библиотеку requests для выполнения HTTP-запросов

url = "http://quotes.toscrape.com/"  # Задаем URL-адрес веб-страницы, которую будем сканировать

response = requests.get(url)  # Выполняем GET-запрос к указанному URL и сохраняем ответ

html = response.text  # Получаем текст HTML из ответа

soup = BeautifulSoup(html, "html.parser")  # Создаем объект BeautifulSoup для парсинга HTML-кода

links = soup.find_all("a")  # Находим все теги <a> в HTML (это ссылки)

for link in links:  # Проходим по всем найденным ссылкам
    print(link.get("href"))  # Извлекаем и выводим значение атрибута href каждой ссылки