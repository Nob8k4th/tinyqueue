from .task import Task


class Queue:
    def __init__(self, priority_mode: bool = False) -> None:
        self.priority_mode = priority_mode
        self._items: list[Task] = []

    def enqueue(self, task: Task) -> None:
        self._items.append(task)

    def dequeue(self) -> Task | None:
        if not self._items:
            return None
        if not self.priority_mode:
            return self._items.pop(0)
        index = min(range(len(self._items)), key=lambda i: self._items[i].priority)
        return self._items.pop(index)

    def size(self) -> int:
        return len(self._items)
