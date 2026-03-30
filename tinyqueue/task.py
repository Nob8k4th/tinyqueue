from dataclasses import dataclass


@dataclass
class Task:
    id: str
    payload: object
    priority: int = 0
    status: str = "pending"
    retry_count: int = 0
