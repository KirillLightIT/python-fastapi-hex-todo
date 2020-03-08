from typing import Callable, Iterable

from todolist.domains.todo.entities.todo_item import TodoItem


_FetchAllFnType = Callable[[], Iterable[TodoItem]]


def get_all_todo_items(fetch_all: _FetchAllFnType) -> Iterable[TodoItem]:
    return fetch_all()