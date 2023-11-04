from customtkinter import *
from tkinter import filedialog
from tkinter import messagebox
import os

credit = """Made By Ravisharma on 12-09-2023
 
 
from customtkinter import *
from tkinter import filedialog
from tkinter import messagebox
import os

def credits():
    app = CTk()
    app.title(">>>Credit and Code<<<")
    textbox=CTkTextbox(app,width=500,height=500)
    textbox.pack()
    textbox.insert("0.0",credit)
    textbox.configure(state='disabled')
    app.mainloop()


def folder_genrate():
    text = mainfolder.get("1.0", 'end-1c')
    text2 = subfolder.get("1.0", 'end-1c')
    mainfolder_names = list(set(text.split("\n")))
    subfolder_names = list(set(text2.split("\n")))
    if mainfolder_names[0]=="Enter Main Folders Names":
        mainfolder_names.pop(0)
    if subfolder_names[0]=="Enter Sub Folders Names":
        subfolder_names.pop(0)
    try:
        path = filedialog.askdirectory()
        for main_names in mainfolder_names:
            if not os.path.exists(f"{path}/{main_names}"):
                os.mkdir(f"{path}/{main_names}")
                for sub_names in subfolder_names:
                    if not os.path.exists(f"{path}/{main_names}/{sub_names}"):
                        os.mkdir(f"{path}/{main_names}/{sub_names}")
        messagebox.showinfo("Work Done!", "Folders are generated successfully!!!")
        mainfolder_names.clear()
        subfolder_names.clear()
        clear()
    except Exception as e:
        messagebox.showerror("Error occurred!!!","Can't create the folders!!!")


def clear():
    mainfolder.delete("0.0","end")
    subfolder.delete("0.0","end")

if __name__ == '__main__':
    root = CTk()
    root.title("Folder Maker Ultra ")
    root.geometry("515x340")
    root.minsize(515,360)
    root.maxsize(515,360)
    mainfolder = CTkTextbox(root,width=250,height=250,border_width=2,border_color="lightblue",scrollbar_button_color="lightblue")
    mainfolder.insert("0.0","Enter Main Folders Names")
    mainfolder.grid(row=0,column=0,pady=10)
    subfolder = CTkTextbox(root,width=250,height=250,border_width=2,border_color="lightblue",scrollbar_button_color="lightblue")
    subfolder.insert("0.0", "Enter Sub Folders Names")
    subfolder.grid(row=0,column=1)
    CTkButton(root,text="Genrate" ,command=folder_genrate,hover_color="green").grid(row=1,column=0,padx=60)
    CTkButton(root,text="Clear" ,command=clear,hover_color="red").grid(row=1,column=1,pady=10)
    CTkButton(root,text="Credit & Code" ,command=credits,hover_color="navy").grid(row=2,columnspan=2,pady=10,sticky='ew')
    root.mainloop()
    
    
    --------------------------------------------------------
    CUSTOMTKINTER VERSION = pip install customtkinter==5.2.0
    --------------------------------------------------------
"""


def credits():
    app = CTk()
    app.title(">>>Credit and Code<<<")
    textbox = CTkTextbox(app, width=800, height=800)
    textbox.pack()
    textbox.insert("0.0", credit)
    textbox.configure(state='disabled')
    app.mainloop()


def folder_genrate():
    text = mainfolder.get("1.0", 'end-1c')
    text2 = subfolder.get("1.0", 'end-1c')
    mainfolder_names = list(set(text.split("\n")))
    subfolder_names = list(set(text2.split("\n")))
    if mainfolder_names[0] == "Enter Main Folders Names":
        mainfolder_names.pop(0)
    if subfolder_names[0] == "Enter Sub Folders Names":
        subfolder_names.pop(0)
    try:
        path = filedialog.askdirectory()
        for main_names in mainfolder_names:
            if not os.path.exists(f"{path}/{main_names}"):
                os.mkdir(f"{path}/{main_names}")
                for sub_names in subfolder_names:
                    if not os.path.exists(f"{path}/{main_names}/{sub_names}"):
                        os.mkdir(f"{path}/{main_names}/{sub_names}")
        messagebox.showinfo("Work Done!", "Folders are generated successfully!!!")
        mainfolder_names.clear()
        subfolder_names.clear()
        clear()
    except Exception as e:
        messagebox.showerror("Error occurred!!!", "Can't create the folders!!!")


def clear():
    mainfolder.delete("0.0", "end")
    subfolder.delete("0.0", "end")


if __name__ == '__main__':
    root = CTk()
    root.title("Folder Maker Ultra ")
    root.geometry("515x330")
    root.minsize(515, 330)
    root.maxsize(515, 360)
    mainfolder = CTkTextbox(root, width=250, height=250, border_width=2, border_color="lightblue",
                            scrollbar_button_color="lightblue")
    mainfolder.insert("0.0", "Enter Main Folders Names")
    mainfolder.grid(row=0, column=0, pady=10)
    subfolder = CTkTextbox(root, width=250, height=250, border_width=2, border_color="lightblue",
                           scrollbar_button_color="lightblue")
    subfolder.insert("0.0", "Enter Sub Folders Names")
    subfolder.grid(row=0, column=1)
    CTkButton(root, text="Genrate", command=folder_genrate, hover_color="green").grid(row=1, column=0, padx=60)
    CTkButton(root, text="Clear", command=clear, hover_color="red").grid(row=1, column=1, pady=10)
    CTkButton(root, text="Credit & Code", command=credits, hover_color="navy").grid(row=2, columnspan=2, pady=10,
                                                                                    sticky='ew')
    root.mainloop()
