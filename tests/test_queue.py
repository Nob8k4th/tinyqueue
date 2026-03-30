from tinyqueue.queue import Queue
from tinyqueue.task import Task


def test_fifo_enqueue_dequeue():
    queue = Queue()
    queue.enqueue(Task("1", {}))
    queue.enqueue(Task("2", {}))
    assert queue.dequeue().id == "1"


def test_priority_high_first_case_one():
    queue = Queue(priority_mode=True)
    queue.enqueue(Task("low", {}, priority=1))
    queue.enqueue(Task("high", {}, priority=10))
    assert queue.dequeue().id == "high"


def test_priority_high_first_case_two():
    queue = Queue(priority_mode=True)
    queue.enqueue(Task("a", {}, priority=3))
    queue.enqueue(Task("b", {}, priority=8))
    queue.enqueue(Task("c", {}, priority=1))
    assert queue.dequeue().id == "b"


def test_size():
    queue = Queue()
    queue.enqueue(Task("x", {}))
    assert queue.size() == 1


def test_empty_dequeue_none():
    assert Queue().dequeue() is None
