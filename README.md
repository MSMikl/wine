# Новое русское вино

Сайт магазина авторского вина "Новое русское вино".

## Подготовка входных данных

Данные для каталога вин считываются из файла `wines.xlsx`, который находится в папке с программой. Для изменения каталога следует отредактировать файл в соответствии со следующим форматом:

| Категория | Название | Сорт | Цена | Картинка |
|-----------|----------|------|------|----------|
| Белые вина | Белая леди | Дамский пальчик | 399 | belaya_ledi.png

Также можно передать вместо `wines.xlsx` свой файл - для этого следует создать в папке программы файл `.env` и указант ьв нем путь к файлу с данными в следующем формате

      XLSX_PATH = wines.xlsx

Изображения бутылок находятся в папке `images`

## Запуск

- Скачайте код
- Установите зависимости командой

      pip install -r requirements.txt
   
- Запустите сайт командой

      python3 main.py

- Перейдите на сайт по адресу [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
