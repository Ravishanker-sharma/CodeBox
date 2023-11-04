from customtkinter import *
from tkinter import Listbox
import datetime
import time
from plyer import notification
import multiprocessing
from pushbullet import Pushbullet




selected_task_index = None

'''def tommrow_task_app():
    def save_tasks(file_name="tommorow's_task.txt"):
        with open(file_name, "w") as file:
            tasks = listbox1.get(0, END)
            for task in tasks:
                file.write(task + "\n")
    def add_task():
        task = entry1.get()
        if task:
            listbox1.insert(END, task)
            entry1.delete(0, END)
            save_tasks()

    def delete_task():
        selected_task = listbox1.curselection()
        if selected_task:
            listbox1.delete(selected_task[0])
            save_tasks()

    def load_tasks(file_name="tommorow's_task.txt"):
        try:
            with open(file_name, "r") as file:
                tasks = file.readlines()
                for task in tasks:
                    listbox1.insert(END, task.strip())
        except FileNotFoundError:
            pass
    app = CTk()
    app.geometry()
    listbox1 = Listbox(app, selectmode=SINGLE, height=15, width=27,font='Helvetica 20 bold',borderwidth=5,background="#145369",foreground="white")
    listbox1.grid(rowspan=10,columnspan=2,pady=10,padx=10)
    entry1 = CTkEntry(app,width=320)
    entry1.grid(row=11,column=0,columnspan=2)
    CTkButton(app, text='Add task', command=add_task).grid(pady=10,row=12,column=0)
    CTkButton(app, text='Delete task', command=delete_task).grid(row=12,column=1)
    load_tasks("tommorow's_task.txt")
    app.mainloop()'''


def mobile_notifications(API_key):
    file = "today's_task.txt"
    with open(file, "r") as f:
        text = f.read()

    pb = Pushbullet(API_key)
    push = pb.push_note("Undone Tasks", text)
def notify_task():
    def loader(file_name="today's_task.txt"):
        msg=""
        try:
            with open(file_name, "r") as file:
                tasks = file.readlines()
                for task in tasks:
                    msg=msg+task
        except:
            pass
        return msg
    while True:
        notification_title = "Pending Task for the Day"
        notification_text = loader()
        notification_timeout = 2  # Notification will disappear after 1 seconds
        name_of_app="Notifier Pro"

        notification.notify(
            app_name=name_of_app,
            title=notification_title,
            message=notification_text,
            timeout=notification_timeout,
        )
        time.sleep(5)

def update_date():
    current_date = datetime.datetime.now().strftime('%Y-%m-%d')
    current_time = time.strftime('%H:%M:%S')
    date_label.configure(text=f"{current_date} ~ {current_time}")
    root.after(1000, update_date)


def add_task():
    task = entry.get()
    if task:
        listbox.insert(END, task)
        entry.delete(0, END)
        save_tasks()

def delete_task():
    global selected_task_index
    if selected_task_index is not None:
        listbox.delete(selected_task_index)
        selected_task_index = None  # Reset the selected task index
        save_tasks()

def toggle_task_done(event):
    global selected_task_index
    selected_task = listbox.curselection()
    if selected_task:
        task_index = selected_task[0]
        task_text = listbox.get(task_index)
        if task_text.startswith("[✓]"):
            # Task is marked as done, so mark it as undone
            task_text = task_text[3:]  # Remove "[Done] " prefix
        else:
            # Task is not marked as done, so mark it as done
            task_text = "[✓]" + task_text
        listbox.delete(task_index)
        listbox.insert(END, task_text)
        save_tasks()
        selected_task_index = task_index

def save_tasks(file_name="today's_task.txt"):
    with open(file_name, "w") as file:
        tasks = listbox.get(0,END)
        for task in tasks:
            file.write(task + "\n")

def load_tasks(file_name="today's_task.txt"):
    try:
        with open(file_name, "r") as file:
            tasks = file.readlines()
            for task in tasks:
                listbox.insert(END, task.strip())
    except FileNotFoundError:
        pass

def main_app():
    global root, listbox, entry, add_task_button, delete_task_button, date_label, slider
    root = CTk()
    root.geometry()
    listbox = Listbox(root, selectmode=SINGLE, height=15, width=27,font='Helvetica 20 bold',borderwidth=5,background="#145369",foreground="white")
    listbox.grid(rowspan=10,columnspan=2,pady=10,padx=10)
    entry = CTkEntry(root,width=285)
    entry.grid(row=11,column=0,columnspan=2)
    listbox.bind("<ButtonRelease-1>", toggle_task_done)
    CTkButton(root, text='Add task', command=add_task).grid(pady=10,row=12,column=0)
    CTkButton(root, text='Delete task', command=delete_task).grid(row=12,column=1)
    #CTkButton(root, text='''Tomorrow's Task''', command=tommrow_task_app).grid(column=2)
    date_label = CTkLabel(root,font=("arial", 20),fg_color='#145369',text_color="white",corner_radius=10)
    date_label.grid(row=0,column=2,padx=30)
    update_date()
    load_tasks()
    root.mainloop()


if __name__ == '__main__':
    m1=multiprocessing.Process(target=main_app)
    m2=multiprocessing.Process(target=notify_task)
    m1.start()
    m2.start()