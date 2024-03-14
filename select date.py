import os
import datetime
from shutil import copyfileobj
import tkinter as tk
from tkinter import messagebox
from tkcalendar import Calendar
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

