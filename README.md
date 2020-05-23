Поисковой бот канала [Рекомендации подкастов](http://t.me/podrec) 
========

- Бот для поиска русскоязычных подкастов по ключевым словам. 
- Искать можно в Apple Podcasts, Google Podcasts и Яндексе.
- Бот выдает до 5 первых результатов ссылкой. 

<a href="https://i.ibb.co/7CZyS1K/screenshot.jpg" target="new"><img src="https://i.ibb.co/pwMX1Ld/screenshot.jpg" alt="screenshot" border="0"></a>

Installing
----------
Для загрузки репозитория выполните в консоли:
```
git clone https://github.com/DianaPrs/Podrecbot.git
```
Создайте виртуальное окужение и установите пакеты:
```
pip install -r requirements.txt
```
Запустите созданное окружение.

Settings
--------
Создайте файл settings.py и добавьте туда следующие настройки:
```
API_KEY = "API_ключ_от_BotFather"

PROXY = "Данные_прокси"

KEY = "API_ключ_для_СПП"

CSE = "Идентификатор поисковой системы"
```

Подробнее о создании СПП и получении ключа [здесь](https://developers.google.com/custom-search/v1/overview)

Launch
------
Для запуска бота выполнить:
```
python bot.py
```
    
