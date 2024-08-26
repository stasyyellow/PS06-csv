import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

# Инициализация
driver = webdriver.Chrome()

url = "https://www.divan.ru/category/svet"
driver.get(url)

time.sleep(7)

# Находим карточки с товарами на сайте
products = driver.find_elements(By.CLASS_NAME, '_Udok U4KZV')

# Создаём список, в который потом всё будет сохраняться
parsed_data = []

# Перебираем коллекцию продуктов
for product in products:
    try:
        # Находим элементы внутри карточек по актуальным селекторам
        title = product.find_element(By.CSS_SELECTOR, 'ui-GPFV8 qUioe ProductName ActiveProduct cursor-on-hover').text #<a tabindex="0" class="ui-GPFV8 qUioe ProductName ActiveProduct cursor-on-hover" href="/product/podvesnoj-svetilnik-sanset-black"><span itemprop="name" class="cursor-on-hover">Подвесной светильник Сансет Black</span></a> |  <span itemprop="name" class="cursor-on-hover">Подвесной светильник Сансет Black</span>
        price = product.find_element(By.CSS_SELECTOR, 'q5Uds fxA6s').get_attribute('content')       # price = product.find_element(By.CSS_SELECTOR, 'meta[itemprop="price"]').get_attribute('content') #<div class="q5Uds fxA6s"><span class="ui-LD-ZU KIkOH" data-testid="price">5190<span class="ui-i5wwi ui-VDyJR ui-VWOa-">руб.</span></span><span class="ui-LD-ZU ui-SVNym bSEDs" data-testid="price">5990<span class="ui-i5wwi ui-VDyJR ui-VWOa-">руб.</span></span><div class="ui-Mqn8h ui-6Ys-Y dW3QK"><div class="ui-JhLQ7">-13%</div></div></div>
        link = product.find_element(By.CSS_SELECTOR, 'https://www.divan.ru/product/podvesnoj-svetilnik-sanset-black').get_attribute('href')

    #Вносим инфу в список
        parsed_data.append([title, price, link])

    except Exception as e:
        print(f"Произошла ошибка при парсинге: {e}")
        continue

driver.quit()

with open("divna_products.csv", 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # Создаём первый ряд
    writer.writerow(['Название продукта', 'Цена', 'Ссылка на продукт'])
    # Прописываем использование списка как источника для рядов таблицы
    writer.writerows(parsed_data)

print("Парсинг завершен и данные сохранены в файл divan_products.csv")





# import time
# import csv
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# # Инициализация
# driver = webdriver.Chrome()
#
# url = "https://www.divan.ru/"
# driver.get(url)
#
# time.sleep(7)
#
# # Находим все карточки с товарами на сайте

# products = driver.find_elements(By.CLASS_NAME, 'c9h0M')  # Пример класса
#
# # Создаём список, в который потом всё будет сохраняться
# parsed_data = []
#
# # Перебираем коллекцию продуктов

# for product in products:
#     try:
#         # Находим элементы внутри продуктов по значению
#         # Находим названия продуктов <span itemprop="name" class="cursor-on-hover">Подвесной светильник Сансет Black</span>
#         title = product.find_element(By.CSS_SELECTOR, 'span.cursor-on-hover').text
#         # Находим цены <span class="ui-LD-ZU KIkOH" data-testid="price">5190<span class="ui-i5wwi ui-VDyJR ui-VWOa-">руб.</span></span>
#         price = product.find_element(By.CSS_SELECTOR, 'span.ui-LD-ZU KIkOH').text
#         # Находим ссылку на продукт <a tabindex="0" class="ui-GPFV8 qUioe ProductName ActiveProduct cursor-on-hover" href="/product/podvesnoj-svetilnik-sanset-black"><span itemprop="name" class="cursor-on-hover">Подвесной светильник Сансет Black</span></a>
#         link = product.find_element(By.CSS_SELECTOR, 'a.https://www.divan.ru/category/svet/product/podvesnoj-svetilnik-sanset-black"').get_attribute('href')
#
#         # Вносим найденную информацию в список
#         parsed_data.append([title, price, link])
#
#     except Exception as e:
#         print(f"Произошла ошибка при парсинге: {e}")
#         continue
#
# # Закрываем подключение браузера
# driver.quit()
#
# # Прописываем открытие нового файла, задаём ему название и форматирование
# with open("divna_products.csv", 'w', newline='', encoding='utf-8') as file:
#     # Используем модуль csv и настраиваем запись данных в виде таблицы
#     writer = csv.writer(file)
#     # Создаём первый ряд
#     writer.writerow(['Название продукта', 'Цена', 'Ссылка на продукт'])
#     # Прописываем использование списка как источника для рядов таблицы
#     writer.writerows(parsed_data)
#
# print("Парсинг завершен и данные сохранены в файл divan_products.csv")



import scrapy
#
# class LightingSpider(scrapy.Spider):
#     name = 'lighting'
#     allowed_domains = ['divan.ru']
#     start_urls = ['https://www.divan.ru/category/svet']
#
#     def parse(self, response):
#         self.log(f'Parsing page: {response.url}')
#         # Используем CSS селектор для извлечения ссылок на продукты
#         product_links = response.css('a[href*="/product/"]::attr(href)').getall()
#         self.log(f'Found {len(product_links)} product links')
#
#         if not product_links:
#             self.log('No product links found!')
#         for link in product_links:
#             yield response.follow(link, self.parse_product)
#
#         # Проверяем наличие следующей страницы
#         next_page = response.css('a.pagination__next::attr(href)').get()
#         if next_page:
#             self.log(f'Next page found: {next_page}')
#             yield response.follow(next_page, self.parse)
#         else:
#             self.log('No next page link found!')
#
#     def parse_product(self, response):
#         # Извлекаем название и цену продукта
#         name = response.css('h1[itemprop="name"]::text').get()
#         price = response.css('span[itemprop="price"]::attr(content)').get()
#         self.log(f'Parsed product: {name} - {price}')
#
#         if not name or not price:
#             self.log(f'Missing data on {response.url}')
#         yield {
#             'name': name,
#             'price': price,
#             'link': response.url
#         }