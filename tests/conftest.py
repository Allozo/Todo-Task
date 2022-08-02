import pytest

from app.todo_list import ToDoList


@pytest.fixture()
def empty_todo():
    return ToDoList()


@pytest.fixture()
def todo_with_preset() -> ToDoList:
    todo = ToDoList()

    todo.add('Купить хлеб')
    todo.add('Купить молоко')
    todo.add('Купить масло')

    todo.finish_id(0)
    todo.finish_id(2)

    return todo
