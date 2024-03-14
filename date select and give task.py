import os
import datetime
from shutil import copyfileobj
import tkinter as tk
from tkinter import messagebox
from tkcalendar import Calendar
from time import sleep

today = f"{(datetime.date.today())}.txt"
yesterday = f"{(datetime.date.today()) - datetime.timedelta(days=1)}.txt"
tomorrow = f"{(datetime.date.today()) + datetime.timedelta(days=1)}.txt"
print(today)


def selectdate():
    def date_selected(event):
        selected_date = cal.get_date()
        selected_date_label.config(text=f"Selected Date: {selected_date}")

    def disable_dates(date):
        # Return True to enable selection, False to disable
        today = date.today()
        return date >= today

    def exit_app():
        current_date = datetime.date.today()
        specific_date = datetime.date.fromisoformat(cal.get_date())
        if specific_date < current_date:
            messagebox.showerror("DATE ALREADY PASSED", 'Bruh! Are you serious?\nWant to schedule TASK in past :/')
        elif specific_date == current_date:
            messagebox.showerror("SELECTED DATE IS TODAY", "Bruh! Wake up this date is TODAY only.\nTry scheduling the "
                                                           "task directly")
            root.quit()
        else:
            root.quit()

    root = tk.Tk()
    root.title("Date Selection App")

    cal = Calendar(
        root,
        date_pattern="yyyy-mm-dd",
        selectbackground="blue",
        date_disabled_callback=disable_dates,
    )
    cal.pack(padx=10, pady=10)

    cal.bind("<<CalendarSelected>>", date_selected)

    exit_button = tk.Button(root, text="Select Date", command=exit_app)
    exit_button.pack(pady=5)

    selected_date_label = tk.Label(root, text="Selected Date: ")
    selected_date_label.pack(pady=5)

    root.mainloop()

    return cal.get_date()

def transfertask():
    if not os.path.exists("Startfile"):
        with open("Startfile", 'w') as f:
            f.write("")
        with open(f"{today}.txt", 'w') as h:
            h.write("")

    else:
        if os.path.exists(yesterday):
            if os.path.exists(today):
                with open(yesterday, "rb") as src, open(today, "ab") as dest:
                    copyfileobj(src, dest)
                os.remove(yesterday)
            else:
                with open(today, 'w') as h:
                    h.write("")
                with open(yesterday, "rb") as src, open(today, "ab") as dest:
                    copyfileobj(src, dest)
                os.remove(yesterday)

    sleep(1)