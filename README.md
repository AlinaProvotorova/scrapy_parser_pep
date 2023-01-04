#### scrapy_parser_pep
# Парсер PEP документов Python

Парсер, который умеет:
1. Собирать и записывать информацию о всех документах PEP;
2. Собирать и записывать информацию о количестве статусов существующих в PEP;

### Запуск парсера:
- Клонируйте проект
- Установите библиотеки командой:
```
(venv) ...$ pip install -r requirements.txt
```

### Режимы работы парсера:

в терминале введите команду:

```
(venv) ...$ scrapy crawl pep

```

После запуска парсера будет создана директория 'results' с актуальными файлами:

- Файл с информацией о каждом документе PEP 
- Файл с информацией о количестве статусов существующих в PEP
```
pep_2023-01-04T22-31-00.csv
status_summary_2023-01-05_03-31-18.csv
```
При каждом новом запуске будут созданы новые актуальные файлы с указанием даты

Автор: [Провоторова Алина Игоревна](https://t.me/alinamalina998)



