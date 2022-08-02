from dataclasses import dataclass
from enum import Enum


class NameStatusTask(Enum):
    Finish = 'FINISH'
    Active = 'ACTIVE'


@dataclass
class Task:
    id_task: int
    name: str
    status: str = NameStatusTask.Active.value
