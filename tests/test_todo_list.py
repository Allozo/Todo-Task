import pytest

from app.task import Task
from app.todo_list import ToDoList


def from_list_task_to_list_task_name(list_task: list[Task]):
    return [task.name for task in list_task]


def test_add_task(empty_todo: ToDoList):
    name_task = 'Купить молоко'

    empty_todo.add(name_task)

    assert "Task(id_task=0, name='Купить молоко', status='ACTIVE')" == str(
        empty_todo[0]
    )


def test_finish_id_task(empty_todo: ToDoList):
    name_task = 'Купить молоко'

    empty_todo.add(name_task)
    empty_todo.finish_id(0)

    assert "Task(id_task=0, name='Купить молоко', status='FINISH')" == str(
        empty_todo[0]
    )


def test_finish_name_task_correct(empty_todo: ToDoList):
    name_task_milk = 'Купить молоко'
    name_task_bread = 'Купить хлеб'

    empty_todo.add(name_task_milk)
    empty_todo.add(name_task_bread)
    empty_todo.finish_name('Купить молоко')

    assert "Task(id_task=0, name='Купить молоко', status='FINISH')" == str(
        empty_todo[0]
    )


def test_finish_name_task_error(empty_todo: ToDoList):
    name_task_milk = 'Купить молоко'
    name_task_bread = 'Купить хлеб'

    empty_todo.add(name_task_milk)
    empty_todo.add(name_task_bread)

    with pytest.raises(ValueError):
        empty_todo.finish_name('Сделать 3 домашнюю работу')

    with pytest.raises(ValueError):
        empty_todo.finish_name('Купить')


def test_finish_task(todo_with_preset: ToDoList):
    right_res = ['Купить хлеб', 'Купить масло']
    res = todo_with_preset.finish_task

    assert right_res == from_list_task_to_list_task_name(res)


def test_active_task(todo_with_preset: ToDoList):
    right_res = ['Купить молоко']
    res = todo_with_preset.active_task

    assert right_res == from_list_task_to_list_task_name(res)


def test_all_task(todo_with_preset: ToDoList):
    right_res = ['Купить хлеб', 'Купить молоко', 'Купить масло']
    res = todo_with_preset.all_task

    assert right_res == from_list_task_to_list_task_name(res)
