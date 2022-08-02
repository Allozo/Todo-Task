from pathlib import Path

from app.app import app, render_active_task, render_all_task, render_finish_task
from app.todo_list import ToDoList


def is_equal_text(text1: str, text2: str):
    return str(text1.replace('    ', '')) == str(text2.replace('    ', ''))


def test_render_all_task(todo_with_preset: ToDoList):
    file_path = Path('tests/attachments/all_task.html')

    if file_path.exists():
        with file_path.open(encoding='utf-8') as file:
            right_render = file.read()

    with app.app_context():
        new_render = render_all_task(todo_with_preset)

    assert is_equal_text(right_render, new_render)


def test_render_active_task(todo_with_preset: ToDoList):
    file_path = Path('tests/attachments/active_task.html')

    if file_path.exists():
        with file_path.open(encoding='utf-8') as file:
            right_render = file.read()

    with app.app_context():
        new_render = render_active_task(todo_with_preset)

    assert is_equal_text(right_render, new_render)


def test_render_finish_task(todo_with_preset: ToDoList):
    file_path = Path('tests/attachments/finish_task.html')

    if file_path.exists():
        with file_path.open(encoding='utf-8') as file:
            right_render = file.read()

    with app.app_context():
        new_render = render_finish_task(todo_with_preset)

    assert is_equal_text(right_render, new_render)
