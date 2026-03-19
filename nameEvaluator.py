import tkinter as tk
import random
from PIL import Image, ImageTk

def loadImage(path):
    img = Image.open(path)
    img = img.resize((120, 120))
    return ImageTk.PhotoImage(img)

# Preload images
happyFace = loadImage("happy.webp")
neutralFace = loadImage("neutral.png")
sadFace = loadImage("sad.jpg")

def gradeName():
    name = entry.get()

    if name.strip() == "":
        result_label.config(text="Enter a name!", fg="red")
        image_label.config(image="")
        return

    score = random.randint(0, 100)

    if score >= 80:
        mood = "Great name!"
        img = happyFace
        color = "green"
    elif score >= 50:
        mood = "It's okay!"
        img = neutralFace
        color = "orange"
    else:
        mood = "Not great..."
        img = sadFace
        color = "red"

    result_label.config(text=f"{name}: {score}/100\n{mood}", fg=color)

    image_label.config(image=img)
    image_label.image = img

root = tk.Tk()
root.geometry("400x400")

entry = tk.Entry(root)
entry.pack(pady=10)

tk.Button(root, text="Grade", command=gradeName).pack()

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

image_label = tk.Label(root)
image_label.pack(pady=10)

root.mainloop()