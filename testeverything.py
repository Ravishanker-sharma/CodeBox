import tkinter as tk
from tkinter import PhotoImage

app = tk.Tk()
app.title("Resized Image on Canvas")

canvas = tk.Canvas(app, width=400, height=300)
canvas.pack()

image = PhotoImage(file="7IsD.gif")  # Replace with your image path

x1, y1, x2, y2 = 100, 50, 300, 250
resized_image = image.subsample(2, 2)

canvas.create_image(x1, y1, anchor=tk.NW, image=resized_image)

app.mainloop()
