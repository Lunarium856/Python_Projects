class Project:
    def __init__(self, projectID, name, desc, time_create, time_update, tasks, progress):
        self.projectID = projectID
        self.name = name
        self.desc = desc
        self.time_create = time_create
        self.time_update = time_update
        self.tasks = tasks
        self.progress = progress

    def Edit():
        pass

    def Delete():
        pass

class Task:
    def __init__(self, taskID, name, desc, weight, subtasks):
        self.taskID = taskID
        self.name = name
        self.desc = desc
        self.weight = weight
        self.subtasks = subtasks

    def Edit():
        pass

    def Delete():
        pass

class Subtask:
    def __init__(self, subtaskID, name, desc, weight):
        pass
    
    def Edit():
        pass

    def Delete():
        pass