class Project:
    def __init__(self, projectID, name, desc, time_create, time_update, tasks, tags, progress):
        self.projectID = projectID
        self.name = name
        self.desc = desc
        self.time_create = time_create
        self.time_update = time_update
        self.tasks = tasks
        self.tags = tags
        self.progress = progress

class Task:
    def __init__(self, taskID, name, desc, weight, tags, subtasks):
        self.taskID = taskID
        self.name = name
        self.desc = desc
        self.weight = weight
        self.tags = tags
        self.subtasks = subtasks

class Subtask:
    def __init__(self, subtaskID, name, desc, tags, weight):
        self.subtaskID = subtaskID
        self.name = name
        self.desc = desc
        self.tags = tags
        self.weight = weight

class Tag:
    def __init__(self, tagID, name, desc, colour):
        self.tagID = tagID
        self.name = name
        self.desc = desc
        self.colour = colour
    