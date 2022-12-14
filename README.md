# todo_task

## Description:

Данный проект представляет из себя простейшее ToDo приложение, в котором можно вести список дел. Проект состоит из двух частей: модуль `todo_list.py` содержит модуль, который позволяет хранить задачи, помечает их выполнение; модуль flask-приложения, который позволяет запустить работу на сервере.

## Create venv:

Для создания виртуального окружения воспользуйтесь командой:

```
make venv
```

Для активации виртуального окружения на windows можно воспользоваться командой:

```
.venv\Scripts\activate.bat
```

## Run application

Для запуска приложения выполните команду:

```
make run
```

Чтобы воспользоваться приложением перейдите на страницу `http://127.0.0.1:5000/`.

## Run tests:

```
make test
```

## Run linters:

```
make lint
```

## Run formatters:
```
make format
```
