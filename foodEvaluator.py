import tkinter as tk
import random
from PIL import Image, ImageTk

def loadImage(path):
    img = Image.open(path)
    img = img.resize((120, 120))
    return ImageTk.PhotoImage(img)

def judgeFood():
    food = entry.get()

    if food.strip() == "":
        result_label.config(text="Wus your favorite food?", fg="blue")
        image_label.config(image="")
        return

    score = random.randint(0, 100)

    if score >= 80:
        mood = "DELICIOUS!"
        img = happyFace
        color = "green"
    elif score >= 50:
        mood = "Yeah it's aight"
        img = neutralFace
        color = "orange"
    else:
        mood = "Ew bruh"
        img = sadFace
        color = "red"

    result_label.config(text=f"{food}: {score}/100\n{mood}", fg=color)

    image_label.config(image=img)
    image_label.image = img

root = tk.Tk()
root.geometry("400x400")

# Preload images
happyFace = loadImage("images/happy.webp")
neutralFace = loadImage("images/neutral.png")
sadFace = loadImage("images/sad.jpg")

entry = tk.Entry(root)
entry.pack(pady=10)

tk.Button(root, text="Grade", command=judgeFood).pack()

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

image_label = tk.Label(root)
image_label.pack(pady=10)

root.mainloop()