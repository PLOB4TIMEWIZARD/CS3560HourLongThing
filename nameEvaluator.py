import tkinter as tk
import random
from PIL import Image, ImageTk

def loadImage(path):
    img = Image.open(path)
    img = img.resize((180, 180))
    return ImageTk.PhotoImage(img)

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
root.geometry("500x500")

happyFace = loadImage("images/happy.webp")
neutralFace = loadImage("images/neutral.png")
sadFace = loadImage("images/sad.jpg")

tk.Label(root, text="Name Grader", font=("Arial", 20)).pack(pady=10)

entry = tk.Entry(root, font=("Arial", 16), width=20)
entry.pack(pady=15)

tk.Button(root, text="Grade", command=gradeName,
          font=("Arial", 14), width=15, height=2).pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=15)

image_label = tk.Label(root)
image_label.pack(pady=15)

root.mainloop()