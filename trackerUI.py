import tkinter as tk
import datetime
from tkinter import ttk
from tracker import TimeTracker

class TimeTrackerUI:
    def __init__(self):
        self.tracker = TimeTracker()
        self.root = tk.Tk()
        self.root.title("Time Tracker")

        # Set background and foreground colors
        self.root.configure(bg="#393c4d")
        ttk.Style().configure("TLabel", foreground="white", background="#393c4d", font=("Helvetica", 10))
        ttk.Style().configure("TButton", foreground="#393c4d", background="red", font=("Helvetica", 10))
        

        # Create project name input
        project_label = ttk.Label(self.root, text="Project Name:")
        project_label.grid(row=0, column=0, padx=5, pady=5)

        self.project_entry = ttk.Entry(self.root)
        self.project_entry.grid(row=0, column=1, padx=5, pady=5)

        # Create task name input
        task_label = ttk.Label(self.root, text="Task Name:")
        task_label.grid(row=1, column=0, padx=5, pady=5)

        self.task_entry = ttk.Entry(self.root)
        self.task_entry.grid(row=1, column=1, padx=5, pady=5)

        # Create buttons
        start_button = ttk.Button(self.root, text="Start", command=self.start)
        start_button.grid(row=2, column=0, padx=5, pady=5)

        end_button = ttk.Button(self.root, text="End", command=self.end)
        end_button.grid(row=2, column=1, padx=5, pady=5)

        report_button = ttk.Button(self.root, text="Generate Report", command=self.generate_report)
        report_button.grid(row=2, column=2, padx=5, pady=5)

        # Create listbox to display started projects
        projects_label = ttk.Label(self.root, text="Started Projects:")
        projects_label.grid(row=3, column=0, padx=5, pady=5)

        self.projects_listbox = tk.Listbox(self.root)
        self.projects_listbox.grid(row=4, column=0, padx=5, pady=5)

        # Populate listbox with started projects
        self.refresh_projects()

    def start(self):
        project_name = self.project_entry.get()
        task_name = self.task_entry.get()
        self.tracker.start_work(project_name, task_name)
        self.refresh_projects()

    def end(self):
        project_name = self.project_entry.get()
        task_name = self.task_entry.get()
        self.tracker.end_work(project_name, task_name)
        self.refresh_projects()

    def generate_report(self):
        report = self.tracker.get_report()
        report_window = tk.Toplevel(self.root)
        report_window.title("Time Tracker Report")

        report_label = tk.Label(report_window, text=report, font=("Helvetica", 12))
        report_label.pack(padx=5, pady=5)

    def refresh_projects(self):
        self.projects_listbox.delete(0, tk.END)
        started_projects = self.tracker.get_started_projects()
        for project_name in started_projects:
            self.projects_listbox.insert(tk.END, project_name)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    tracker_gui = TimeTrackerUI()
    tracker_gui.run()
            