import datetime

# Create an empty dictionary to store project working hours
project_hours = {}

# Function to start working on a project
def start_project(project_name):
    now = datetime.datetime.now()
    project_hours[project_name] = {"start_time": now, "end_time": None}
    print(f"Started working on {project_name} at {now}")

# Function to end working on a project
def end_project(project_name):
    now = datetime.datetime.now()
    if project_name in project_hours:
        project_hours[project_name]["end_time"] = now
        elapsed_time = now - project_hours[project_name]["start_time"]
        print(f"Ended working on {project_name} at {now}. Elapsed time: {elapsed_time}")
    else:
        print(f"You haven't started working on {project_name} yet.")

# Example usage
start_project("Project A")
end_project("Project A")
start_project("Project B")
end_project("Project B")

# Print the working hours for each project
for project_name, project_time in project_hours.items():
    elapsed_time = project_time["end_time"] - project_time["start_time"]
    print(f"{project_name}: {elapsed_time}")
