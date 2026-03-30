# tinyqueue

`tinyqueue` 是一个纯内存任务队列原型，包含任务对象、队列、执行器和简化调度器。

## 组件说明

- `Task`：任务数据结构（id、payload、priority、status、retry_count）
- `Queue`：支持普通 FIFO 与按优先级出队
- `Worker`：执行任务函数并按重试配置处理异常
- `Scheduler`：解析简化 cron 表达式中的执行间隔

## 快速使用

```bash
pip install -e .
```

```python
from tinyqueue import Task, Queue, Worker, Scheduler

q = Queue(priority_mode=True)
q.enqueue(Task(id="t1", payload={"x": 1}, priority=10))
q.enqueue(Task(id="t2", payload={"x": 2}, priority=1))

task = q.dequeue()
print(task.id)

worker = Worker(max_retries=2)
done = worker.run(task, lambda payload: print(payload))
print(done.status)

print(Scheduler().parse_cron("*/5 * * * *"))
```

## 测试

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install -e .
pytest tests/ -v --tb=short --json-report --json-report-file=test_results.json
```
