import logging
import typing as t

from flask import Flask, redirect, render_template, request, url_for

from app.todo_list import ToDoList

if t.TYPE_CHECKING:
    from werkzeug.wrappers.response import Response


app = Flask(__name__)
todo_list = ToDoList()


def render_all_task(todo: ToDoList) -> str:
    return render_template('all_task.html', todo_list=todo.all_task)


def render_finish_task(todo: ToDoList) -> str:
    return render_template('finish_task.html', todo_list=todo.finish_task)


def render_active_task(todo: ToDoList) -> str:
    return render_template('active_task.html', todo_list=todo.active_task)


def validation_task_name_task(task_name: str) -> bool:  # pragma: no cover
    return task_name != ''


@app.route('/all_task')
def all_task() -> str:  # pragma: no cover
    logging.info('Print all task')
    return render_all_task(todo_list)


@app.route('/finish_task')
def finish_task() -> str:  # pragma: no cover
    logging.info('Print finish task')
    return render_finish_task(todo_list)


@app.route('/')
@app.route('/active_task')
def active_task() -> str:  # pragma: no cover
    logging.info('Print active task')
    return render_active_task(todo_list)


@app.route('/set_finish_status/<int:task_id>', methods=['POST'])
def set_finish_status(task_id: int) -> 'Response':  # pragma: no cover
    logging.info('Finish task id: %s', task_id)
    todo_list.finish_id(task_id)
    return redirect(url_for('active_task'))


@app.route('/add_task', methods=['POST'])
def add_task() -> 'Response':  # pragma: no cover
    task_name = str(request.form.get('task_name_str'))
    if validation_task_name_task(task_name):
        logging.info('Get task name: %s', task_name)
        todo_list.add(task_name)
    return redirect(url_for('active_task'))
