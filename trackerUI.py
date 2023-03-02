import tkinter as tk
import datetime
from tracker import TimeTracker

class TimeTrackerUI:
    def __init__(self):
        self.tracker = TimeTracker()
        self.window = tk.Tk()
        self.window.title("Time Tracker")
        
        # Create project name label and entry
        project_label = tk.Label(self.window, text="Project name:")
        project_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.project_entry = tk.Entry(self.window)
        self.project_entry.grid(row=0, column=1, padx=5, pady=5)
        
        # Create task name label and entry
        task_label = tk.Label(self.window, text="Task name:")
        task_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        self.task_entry = tk.Entry(self.window)
        self.task_entry.grid(row=1, column=1, padx=5, pady=5)
        
        # Create start and end buttons
        start_button = tk.Button(self.window, text="Start", command=self.start_work)
        start_button.grid(row=2, column=0, padx=5, pady=5)
        end_button = tk.Button(self.window, text="End", command=self.end_work)
        end_button.grid(row=2, column=1, padx=5, pady=5)
        
        # Create report text widget
        self.report_text = tk.Text(self.window, width=40, height=10)
        self.report_text.grid(row=3, column=0, columnspan=2, padx=5, pady=5)
        
        # Refresh report button
        refresh_button = tk.Button(self.window, text="Refresh Report", command=self.print_report)
        refresh_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)
        
    def start_work(self):
        project_name = self.project_entry.get()
        task_name = self.task_entry.get()
        if project_name and task_name:
            self.tracker.start_work(project_name, task_name)
        else:
            self.report_text.insert(tk.END, "Please enter a project and task name.\n")
    
    def end_work(self):
        project_name = self.project_entry.get()
        task_name = self.task_entry.get()
        if project_name and task_name:
            self.tracker.end_work(project_name, task_name)
        else:
            self.report_text.insert(tk.END, "Please enter a project and task name.\n")
    
    def print_report(self):
        self.report_text.delete("1.0", tk.END)
        report = self.tracker.get_report()
        self.report_text.insert(tk.END, report)
        
    def run(self):
        self.window.mainloop()
        
if __name__ == '__main__':
    tracker_ui = TimeTrackerUI()
    tracker_ui.run()