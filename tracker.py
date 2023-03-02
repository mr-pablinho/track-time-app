import datetime

# Create an empty dictionary to store project working hours
project_hours = {}

# Function to start working on a project and task
def start_work():
    project_name = input("Enter project name: ")
    task_name = input("Enter task name: ")
    now = datetime.datetime.now()
    if project_name not in project_hours:
        project_hours[project_name] = {}
    if task_name not in project_hours[project_name]:
        project_hours[project_name][task_name] = {"start_time": now, "end_time": None}
    else:
        print(f"You're already working on {task_name} in {project_name}.")
        return
    print(f"Started working on {task_name} in {project_name} at {now}")

# Function to end working on a project and task
def end_work():
    project_name = input("Enter project name: ")
    task_name = input("Enter task name: ")
    now = datetime.datetime.now()
    if project_name in project_hours and task_name in project_hours[project_name]:
        project_hours[project_name][task_name]["end_time"] = now
        elapsed_time = now - project_hours[project_name][task_name]["start_time"]
        print(f"Ended working on {task_name} in {project_name} at {now}. Elapsed time: {elapsed_time}")
    else:
        print(f"You haven't started working on {task_name} in {project_name} yet.")

# Example usage
start_work()
end_work()

# Print the working hours for each project and task
for project_name, project_tasks in project_hours.items():
    print(f"Project: {project_name}")
    for task_name, task_time in project_tasks.items():
        elapsed_time = task_time["end_time"] - task_time["start_time"] if task_time["end_time"] is not None else datetime.timedelta(0)
        print(f" - Task: {task_name}, Elapsed time: {elapsed_time}")
