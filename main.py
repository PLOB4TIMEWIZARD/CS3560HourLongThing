import tkinter as tk
import random
from PIL import Image, ImageTk

## Image loading for the faces
def loadImage(path):
    img = Image.open(path)
    img = img.resize((180, 180))
    return ImageTk.PhotoImage(img)

## Controller for all 3 gui menus
class EvaluatorFrame(tk.Frame):

    title  = "Evaluator"
    prompt = "Enter something!"

    def __init__(self, parent, show_frame, images):
        super().__init__(parent)
        self.show_frame = show_frame
        self.images     = images   # shared dict: happy / neutral / sad

        self._build_nav()
        self._build_ui()

    # Navigation Bar

    def _build_nav(self):
        nav = tk.Frame(self, bg="#222")
        nav.pack(fill="x")

        pages = [
            ("Name",  NameFrame),
            ("Food",  FoodFrame),
            ("Pet",   PetFrame),
        ]
        for label, cls in pages:
            btn = tk.Button(
                nav, text=label,
                bg="#222", fg="white",
                relief="flat", font=("Arial", 11),
                padx=12, pady=6,
                command=lambda c=cls: self.show_frame(c),
            )
            btn.pack(side="left")

    # Main UI

    def _build_ui(self):
        tk.Label(self, text=self.title, font=("Arial", 20)).pack(pady=10)

        self.entry = tk.Entry(self, font=("Arial", 16), width=20)
        self.entry.pack(pady=15)

        tk.Button(
            self, text="Grade", command=self._grade,
            font=("Arial", 14), width=15, height=2,
        ).pack(pady=10)

        self.result_label = tk.Label(self, text="", font=("Arial", 14))
        self.result_label.pack(pady=15)

        self.image_label = tk.Label(self)
        self.image_label.pack(pady=15)

    # Grading

    def _grade(self):
        text = self.entry.get()

        if text.strip() == "":
            self.result_label.config(text=self.prompt, fg="blue")
            self.image_label.config(image="")
            return

        score = random.randint(0, 100)

        if score >= 80:
            img = self.images["happy"]
        elif score >= 50:
            img = self.images["neutral"]
        else:
            img = self.images["sad"]

        mood, color = self.grade(score)

        self.result_label.config(
            text=f"{text}: {score}/100\n{mood}", fg=color
        )
        self.image_label.config(image=img)
        self.image_label.image = img   # keep reference

    def grade(self, score):
        """Override in subclass. Return (mood_str, color_str)."""
        raise NotImplementedError


# Three Evaluators

class NameFrame(EvaluatorFrame):
    title  = "Name Grader"
    prompt = "Enter a name!"

    def grade(self, score):
        if score >= 80:  return "Great name!",        "green"
        if score >= 50:  return "It's okay!",          "orange"
        return               "Not great...",           "red"


class FoodFrame(EvaluatorFrame):
    title  = "Food Grader"
    prompt = "Wus your favorite food?"

    def grade(self, score):
        if score >= 80:  return "DELICIOUS!",          "green"
        if score >= 50:  return "Yeah it's aight",     "orange"
        return               "Ew bruh",                "red"


class PetFrame(EvaluatorFrame):
    title  = "Pet Grader"
    prompt = "Enter a pet! (ex. cat, dog, lizard)"

    def grade(self, score):
        if score >= 80:  return "Great pet!",                          "green"
        if score >= 50:  return "It's an OK pet!",                     "orange"
        return               "Not great... it could use some work",    "red"


# Main Display

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Evaluator App")
        self.geometry("500x500")
        self.resizable(False, False)

        # Load images once, share across all frames
        self.images = {
            "happy":   loadImage("images/happy.webp"),
            "neutral": loadImage("images/neutral.png"),
            "sad":     loadImage("images/sad.jpg"),
        }

        self.frames = {}
        for Page in (NameFrame, FoodFrame, PetFrame):
            frame = Page(self, self.show_frame, self.images)
            self.frames[Page] = frame
            frame.place(relwidth=1, relheight=1)   # stack them on top of each other

        self.show_frame(NameFrame)

    def show_frame(self, page_class):
        self.frames[page_class].tkraise()


if __name__ == "__main__":
    App().mainloop()