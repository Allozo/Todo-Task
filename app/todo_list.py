import logging

from app.task import NameStatusTask, Task

logging.basicConfig(
    level=logging.DEBUG,
    filename='app.log',
    filemode='w',
    format='%(name)s - %(levelname)s - %(message)s',
    encoding='utf-8',
)


class ToDoList:
    def __init__(self) -> None:
        logging.info('Create ToDoList')
        self._base: dict[int, Task] = {}
        self._next_count_id = 0

    def add(self, name: str) -> None:
        logging.info('Add task: %s', name)
        self._base[self._next_count_id] = Task(self._next_count_id, name)
        self._next_count_id += 1

    def finish_id(self, id_task: int) -> None:
        logging.info('Finish task: %d -- %s', id_task, self._base[id_task])
        self._base[id_task].status = NameStatusTask.Finish.value

    def finish_name(self, name_task: str) -> None:
        list_tasks = self.get_tasks_with_name(name_task)
        if len(list_tasks) == 0:
            raise ValueError('Нет задач, которые начинаются с такой строки')
        if len(list_tasks) > 1:
            raise ValueError(
                'Существует несколько задач, которые начинаются с такой строки'
            )
        if len(list_tasks) == 1:
            self.finish_id(list_tasks[0].id_task)

    def __getitem__(self, id_task: int) -> Task:
        logging.info('Get task: %d -- %s', id_task, self._base[id_task])
        return self._base[id_task]

    def get_tasks_with_name(self, start_name: str) -> list[Task]:
        res = []
        for task in self._base.values():
            if task.name.startswith(start_name):
                res.append(task)
        return res

    @property
    def all_task(self) -> list[Task]:
        res = list(self._base.values())
        logging.info('Get all list tasks: %s', res)
        return res

    @property
    def finish_task(self) -> list[Task]:
        res = [
            task
            for task in self._base.values()
            if task.status == NameStatusTask.Finish.value
        ]
        logging.info('Get finish list tasks: %s', res)
        return res

    @property
    def active_task(self) -> list[Task]:
        res = [
            task
            for task in self._base.values()
            if task.status == NameStatusTask.Active.value
        ]
        logging.info('Get active list tasks: %s', res)
        return res
