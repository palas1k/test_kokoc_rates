Django-приложение, которое отображает курс
валюты по отношению к рублю на заданную дату.

## Развертывание
**Установка зависимостей**  
Создать виртуальное окружение в качестве интерпретатора выбрать python 2.7  
Выполнить в консоли команда pip install -r requirements.txt

**Создание файлов с переменными окружения**  
Скопировать данные из файла .env.example в файл .env  
Поставить свои данные в переменные для БД

**Основные команды**

python manage.py                    # Список команд  
python manage.py runserver          # Запуск сервера  
python manage.py createsuperuser    # Создание суперпользователя  

**Миграции**

python manage.py makemigrations         # Создать миграции  
python manage.py migrate                # Применить миграции все миграции  

**Внесение в базу данных**  
Вариант 1:  
открыть консоль # python manage.py shell  
Ввести команду  
 
from rates.services.currencies import update_currency_rate  
update_currency_rate() 

Вариант 2:

Скопировать данные и внести в базу данных вручную через админ панель /admin

{"USD": 91.8237, "TMT": 26.2353, "AZN": 54.0139, "QAR": 25.2263,
"EGP": 29.7232, "IDR": 58.918, "BGN": 50.2962, "AED": 25.003,
"GBP": 115.2296, "DKK": 13.1976, "CAD": 67.7666, "HUF": 25.3272,
"VND": 38.2982, "MDL": 51.6075, "AMD": 22.7146, "UAH": 24.0544,
"XDR": 121.3386, "SEK": 86.9559, "SGD": 68.1134, "HKD": 11.7632,
"GEL": 34.6727, "AUD": 59.5477, "CHF": 103.9788, "KRW": 68.8334,
"CNY": 12.6566, "BYN": 28.417, "NZD": 55.9252, "THB": 25.4052,
"EUR": 98.4099, "TRY": 29.8992, "KGS": 10.2677, "RON": 19.805,
"KZT": 20.5344, "NOK": 86.7661, "RSD": 83.9699, "INR": 11.0663,
"JPY": 61.0692, "CZK": 38.8048, "TJS": 83.8282, "BRL": 18.4682,
"PLN": 22.6753, "UZS": 73.541, "ZAR": 48.3306}

Тогда датой котировок будет день внесения в данных

**Получение данных**

http://127.0.0.1:8000/?charcode=AUD&date=2024-02-16

date - день внесения данных в базу
charcode - значение из списка выше

**Формат строки для crontab**  
01 00 * * * python2 путь до файла/crontab_task.py"

