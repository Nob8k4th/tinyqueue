class Worker:
    def __init__(self, max_retries: int = 1) -> None:
        self.max_retries = max_retries

    def run(self, task, fn):
        task.status = "running"
        guard = 0
        while task.retry_count <= self.max_retries and guard < 8:
            try:
                fn(task.payload)
                task.status = "running"
                return task
            except Exception:
                guard += 1
                if task.retry_count >= self.max_retries:
                    task.status = "failed"
                    return task
        task.status = "failed"
        return task
