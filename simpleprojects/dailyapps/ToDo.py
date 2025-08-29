import os
import tkinter as tk
from tkinter import messagebox, simpledialog
import ttkbootstrap as ttk

# Set the base directory for storing task files
BASE_DIR = r"C:\\Users\\eliha\\vsc\\cove\\python"

def get_project_file():
    """Returns the full file path for the selected project."""
    project = project_var.get()
    return os.path.join(BASE_DIR, f"{project}.txt") if project else os.path.join(BASE_DIR, "tasks.txt")

def load_tasks():
    tasks_file = get_project_file()
    if not os.path.exists(tasks_file):
        return []
    with open(tasks_file, "r") as file:
        return [line.strip() for line in file.readlines()]

def save_tasks(tasks):
    tasks_file = get_project_file()
    with open(tasks_file, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def add_task():
    task = entry_task.get()
    if task:
        tasks = load_tasks()
        tasks.append(task)
        save_tasks(tasks)
        update_listbox()
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

def remove_task():
    try:
        selected_index = listbox_tasks.curselection()[0]
        tasks = load_tasks()
        tasks.pop(selected_index)
        save_tasks(tasks)
        update_listbox()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to remove!")

def update_listbox():
    listbox_tasks.delete(0, tk.END)
    for task in load_tasks():
        listbox_tasks.insert(tk.END, task)

def switch_project(event=None):
    update_listbox()

def add_project():
    new_project = simpledialog.askstring("New Project", "Enter project name:")
    if new_project and new_project not in project_dropdown["values"]:
        project_dropdown["values"] = (*project_dropdown["values"], new_project)
        project_var.set(new_project)
        switch_project()

def remove_project():
    project = project_var.get()
    if project:
        project_path = get_project_file()
        os.remove(project_path) if os.path.exists(project_path) else None
        values = list(project_dropdown["values"])
        values.remove(project)
        project_dropdown["values"] = values
        project_var.set(values[0] if values else "")
        switch_project()

def rename_project():
    old_project = project_var.get()
    if old_project:
        new_project = simpledialog.askstring("Rename Project", "Enter new project name:")
        if new_project and new_project not in project_dropdown["values"]:
            old_path = get_project_file()
            new_path = os.path.join(BASE_DIR, f"{new_project}.txt")
            os.rename(old_path, new_path) if os.path.exists(old_path) else None
            values = list(project_dropdown["values"])
            values[values.index(old_project)] = new_project
            project_dropdown["values"] = values
            project_var.set(new_project)
            switch_project()

def main():
    global entry_task, listbox_tasks, project_var, project_dropdown
    
    root = ttk.Window(themename="darkly")
    root.title("To-Do List")
    root.geometry("400x500")
    root.grid_rowconfigure(2, weight=1)
    root.grid_columnconfigure(0, weight=1)
    
    project_frame = ttk.Frame(root, padding=10)
    project_frame.pack(fill=tk.X, pady=5)
    
    ttk.Label(project_frame, text="Select Project:").pack(side=tk.LEFT, padx=5)
    project_var = ttk.StringVar()
    project_dropdown = ttk.Combobox(project_frame, textvariable=project_var, values=[], state="readonly")
    project_dropdown.pack(side=tk.LEFT, fill=tk.X, expand=True)
    project_dropdown.bind("<<ComboboxSelected>>", switch_project)
    
    btn_add_project = ttk.Button(project_frame, text="+", command=add_project)
    btn_add_project.pack(side=tk.LEFT, padx=2)
    
    btn_remove_project = ttk.Button(project_frame, text="-", command=remove_project)
    btn_remove_project.pack(side=tk.LEFT, padx=2)
    
    btn_rename_project = ttk.Button(project_frame, text="Rename", command=rename_project)
    btn_rename_project.pack(side=tk.LEFT, padx=2)
    
    frame = ttk.Frame(root, padding=10)
    frame.pack(fill=tk.X, pady=10)
    
    entry_task = ttk.Entry(frame)
    entry_task.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
    
    btn_add = ttk.Button(frame, text="Add", command=add_task)
    btn_add.pack(side=tk.LEFT)
    
    listbox_tasks = tk.Listbox(root, bg="#2C2F33", fg="white")
    listbox_tasks.pack(fill=tk.BOTH, expand=True, pady=10)
    
    btn_remove = ttk.Button(root, text="Remove", command=remove_task)
    btn_remove.pack()
    
    root.mainloop()
    
if __name__ == "__main__":
    main()