from dataclasses import dataclass, field
from typing import Optional
from enum import Enum
from datetime import datetime, date


class TaskStatus(Enum):
    TODO = "Task has not been started"
    IN_PROGRESS = "Currently being worked on"
    COMPLETED = "Successfully finished"
    CANCELLED = "Will not be completed"
    
class Priority(Enum):
    LOW = "Can wait"
    MEDIUM = "Normal task"
    HIGH = "Important"
    CRITICAL = "Needs immediate attention"



@dataclass
class Task:
    _counter: int = field(default=0, init=False, repr=False)
    
    id: int = field(init=False)
    _title: str
    description: Optional[str] = None
    status: TaskStatus = TaskStatus.TODO
    priority: Priority = Priority.MEDIUM
    created_at: datetime = datetime.now()
    due_date: Optional[date] = None
    completed_at: Optional[datetime] = None
    
    @property                      # it creates a property object which is binded with title namespace. so we can use the (.getter(), setter(), deleter()) of @property in it.
    def title(self) -> str:
        return self._title
    
    @title.setter             # validation of title before change to title for obj
    def title(self,value: str) -> None:
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Title cannot be empty")
        if len(value.strip()) > 100:
            raise ValueError("Title cannot exceed 100 characters") 
        self._title = value.strip()
        
        
    @property
    def is_overdue(self) -> bool:
        if self.due_date and self.status != TaskStatus.COMPLETED:
            return date.today() > self.due_date
        return False
        
    
    
    # Methods
    
    def start(self) -> None:
        if self.status in (TaskStatus.COMPLETED, TaskStatus.CANCELLED):
            raise ValueError(f"Cannot start a {self.status.name} task.")
        self.status = TaskStatus.IN_PROGRESS
        
    def complete(self) -> None:
        if self.status in TaskStatus.CANCELLED:
            raise ValueError(f"Cannot complete a {self.status.name} task.")
        self.status = TaskStatus.COMPLETED
        self.completed_at = datetime.now()
        
    def cancel(self) -> None:
        if self.status in TaskStatus.COMPLETED:
            raise ValueError(f"Cannot cancel a {self.status.name} task.")
        self.status = TaskStatus.CANCELLED
        
    def reopen(self) -> None:
        if self.status != TaskStatus.COMPLETED:
            raise ValueError("Only completed tasks can be reopened.")
        self.status = TaskStatus.TODO
        
        
    def __str__(self) -> str:
        return f"[{self.priority.name}] {self.title} — {self.status.name}"
    
    
    
    
    
        