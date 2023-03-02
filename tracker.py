import datetime

class TimeTracker:
    def __init__(self):
        self.project_hours = {}

    def start_work(self, project_name, task_name):
        now = datetime.datetime.now()
        if project_name not in self.project_hours:
            self.project_hours[project_name] = {}
        if task_name not in self.project_hours[project_name]:
            self.project_hours[project_name][task_name] = {"start_time": now, "end_time": None}
        else:
            print(f"You're already working on {task_name} in {project_name}.")
            return
        print(f"Started working on {task_name} in {project_name} at {now}")

    def end_work(self, project_name, task_name):
        now = datetime.datetime.now()
        if project_name in self.project_hours and task_name in self.project_hours[project_name]:
            self.project_hours[project_name][task_name]["end_time"] = now
            elapsed_time = now - self.project_hours[project_name][task_name]["start_time"]
            print(f"Ended working on {task_name} in {project_name} at {now}. Elapsed time: {elapsed_time}")
        else:
            print(f"You haven't started working on {task_name} in {project_name} yet.")

    def get_report(self):
        report = ""
        for project_name, project_tasks in self.project_hours.items():
            report += f"Project: {project_name}\n"
            for task_name, task_time in project_tasks.items():
                elapsed_time = task_time["end_time"] - task_time["start_time"] if task_time["end_time"] is not None else datetime.timedelta(0)
                report += f" - Task: {task_name}, Elapsed time: {elapsed_time}\n"
        return report
