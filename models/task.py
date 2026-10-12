from enum import Enum



class Status(Enum):
    TODO = "Yet to start"
    COMPLETED = "Done"

class Task:
    def __init__(self, title : str, description : str | None = None):  # Task()
        self.title = title
        self.description = description or ""
        self.status = Status.TODO   # doesn't have option to change while creating obj
        
    def __str__(self):
        desc_text = f" : {self.description}" if self.description else ""
        return f"[{self.status.value}] - {self.title}{desc_text}"
    
    
    def complete(self):              # obj.complete() [uses the complete() of class Task to change its obj's status] = Task.complete(obj) [we know the complete() is from class Task and we send the obj as self to change its status] 
        if self.status == Status.TODO:
            self.status = Status.COMPLETED
        else:
            print("Task already Done")
        
    def reopen(self):                # Task.reopen(obj)
        if self.status == Status.COMPLETED:
            self.status = Status.TODO
        else:
            print("Task already yet to do")
                
                
"""
        
"""
                
        
        