from tinyqueue.task import Task
from tinyqueue.worker import Worker


def test_task_status_init():
    assert Task("1", {}).status == "pending"


def test_worker_success_updates_done():
    task = Task("1", {"x": 1})
    Worker().run(task, lambda payload: payload)
    assert task.status == "done"


def test_worker_retry_count_incremented():
    task = Task("1", {})

    def fails(_):
        raise RuntimeError("boom")

    Worker(max_retries=1).run(task, fails)
    assert task.retry_count == 1


def test_worker_failed_on_no_retry():
    task = Task("1", {})

    def fails(_):
        raise RuntimeError("boom")

    Worker(max_retries=0).run(task, fails)
    assert task.status == "failed"


def test_worker_retries_correct_count():
    task = Task("1", {})
    call_count = 0

    def fails(_):
        nonlocal call_count
        call_count += 1
        raise RuntimeError("boom")

    Worker(max_retries=3).run(task, fails)
    assert task.retry_count == 3
