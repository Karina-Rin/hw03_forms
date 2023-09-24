# backend_community_homework

[![CI](https://github.com/yandex-praktikum/hw03_forms/actions/workflows/python-app.yml/badge.svg?branch=master)](https://github.com/yandex-praktikum/hw03_forms/actions/workflows/python-app.yml)

## Описание
Форма страницы для публикации постов проект Yatube

### Работа с репозиторим
1. Клонируем репозиторий на локальный компьютер:
```
git clone https://github.com/Karina-Rin/hw03_forms.git
```
2. Переносим в него всю папку `/yatube` из предыдущего репозитория.
3. Переходим в терминале в папку с проектом:
```
cd hw03_forms/
```
4. Развёртываем виртуальное окружение (работаем в VSCode):
* для Mac или Linux:
  ```
  $ python3 -m venv venv
  ```
* для Windows:
  ```
  $ python -m venv venv
  ```
5. Запускаем виртуальное окружение:
* для Mac или Linux:
  ```
  $ source venv/bin/activate
  ```
  
* для Windows:
  ```
  $ source venv/Scripts/activate
  ```
6. Устанавливаем зависимости из файла requirements.txt:
```
$ pip install -r requirements.txt
```
7. Запускаем тесты:
```
$ pytest
```

### Технологии:
* Python 3.7.1
* Pytest 6.2.5
* Flake8 4.0.1
* Django 2.2.6
* Django-debug-toolbar 2.2
