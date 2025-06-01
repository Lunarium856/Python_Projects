import os
import json

class Project:
    def __init__(self, idNo, title, size, priority):
        self.idNo = idNo
        self.title = title
        self.size = size
        self.priority = priority
    
    def to_dict(self):
        return {
            "idNo": self.idNo,
            "title": self.title,
            "size": self.size,
            "priority": self.priority
        }
    
    @staticmethod
    def from_dict(data): # Helper to create Project object from a dictionary
        return Project(data["idNo"], data["title"], data["size"], data["priority"])

# Memory variables
saveFile = 'SaveFile.json'
projects = []

# Load projects from file at startup
try:
    with open(saveFile, 'r') as f:
        data = json.load(f)
        for item in data:
            projects.append(Project.from_dict(item))
except FileNotFoundError:
    print(f"No existing project file '{saveFile}' found. Starting with empty projects.")
except json.JSONDecodeError:
    print(f"Error decoding JSON from '{saveFile}'. Starting with empty projects.")


def save_projects():
    project_dicts = [p.to_dict() for p in projects]
    with open(saveFile, 'w') as f:
        json.dump(project_dicts, f, indent=4) # indent for readability
    print(f"Saved {len(projects)} projects to {saveFile}")


# MENU
while True:
    saveFile.close()

    print("----PROJECT MANAGER MENU----")
    print("[1] Input Project Details     ")
    print("[2] View Projects            *")
    print("[3] Schedule Projects        *")
    print("[4] Get a Project            *")
    print("[5] Exit\n")
    print("(items with * have subsequent menus)")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("ERROR: Invalid input.\n")
        continue

    match choice:
        case 1:
            pass
        case 2:
            while True:
                print(f"Loaded {len(projects)} projects from {saveFile}")
                pass
        case 3:
            pass
        case 4:
            try:
                pass
            except FileNotFoundError:
                pass
        case 5:
            save_projects()
            print("Program Exited")
            break 
        case _:
            print("ERROR: Invalid Input\n")

