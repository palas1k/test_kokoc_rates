Задача: Ваша задача написать Django-приложение, которое будет отображать курс
валюты по отношению к рублю на заданную дату. При обращении к приложению по
адресу http://localhost:8000/rate/?charcode=AUD&date=2024-01-01 , оно должно выводить
результат в виде JSON в формате:
{
"charcode": "AUD",
"date": "2024-01-01",
"rate": 57.0627
}
Данные по валютам должны храниться в базе данных приложения.
А для пополнения этой базы данных нужно написать команду, которая
будет раз в сутки обращаться к сервису ЦБ за актуальными курсами валют по адресу:
https://www.cbr-xml-daily.ru/daily_json.js
Что ожидается в решении:
- джанго приложение
- модель данных (или модели)
- view для отображения валюты на заданную дату
- раздел admin для редактирования данных (через django-admin)
- команда для сбора данных
- формат строки для crontab (как будет запускаться команда)
- инструкция (readme.md), как поднять и настроить проект другому разработчику
Результат работы сохранить в виде отдельного репозитория на github.
Срок выполнения задания: 3 дня.
