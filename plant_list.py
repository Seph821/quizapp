import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random

# Questions grouped by categories
question_bank = {
    "Common from Scientific 1": [
        {
            "question": "Campsis radicans",
            "options": ["Trumpet Creeper", "Flowering Dogwood", "Bradford Pear", "Crepe Myrtle"],
            "answer": "Trumpet Creeper",
            "image_path": "default.jpg"
        },
        {
            "question": "Cornus florida",
            "options": ["Flowering Dogwood", "Bradford Pear", "Crepe Myrtle", "Southern Magnolia"],
            "answer": "Flowering Dogwood",
            "image_path": "default.jpg"
        },
        {
            "question": "Pyrus calleryana",
            "options": ["Bradford Pear", "Crepe Myrtle", "Southern Magnolia", "Virginia Creeper"],
            "answer": "Bradford Pear",
            "image_path": "default.jpg"
        },
        {
            "question": "Lagerstroemia sp.",
            "options": ["Crepe Myrtle", "Southern Magnolia", "Virginia Creeper", "Dogfennel"],
            "answer": "Crepe Myrtle",
            "image_path": "default.jpg"
        },
        {
            "question": "Magnolia grandiflora",
            "options": ["Southern Magnolia", "Virginia Creeper", "Dogfennel", "Pecan"],
            "answer": "Southern Magnolia",
            "image_path": "default.jpg"
        }
    ],
    "Common from Scientific 2": [
        {
            "question": "Parthenocissus Quinquefolia",
            "options": ["Virginia Creeper", "Dogfennel", "Pecan", "Black Cherry"],
            "answer": "Virginia Creeper",
            "image_path": "default.jpg"
        },
        {
            "question": "Eupatorium Capillifolium",
            "options": ["Dogfennel", "Pecan", "Black Cherry", "Water Oak"],
            "answer": "Dogfennel",
            "image_path": "default.jpg"
        },
        {
            "question": "Carya Illinoinensis",
            "options": ["Pecan", "Black Cherry", "Water Oak", "Poison Ivy"],
            "answer": "Pecan",
            "image_path": "default.jpg"
        },
        {
            "question": "Prunus Serotina",
            "options": ["Black Cherry", "Water Oak", "Poison Ivy", "Eastern Redbud"],
            "answer": "Black Cherry",
            "image_path": "default.jpg"
        },
        {
            "question": "Quercus Nigra",
            "options": ["Water Oak", "Poison Ivy", "Eastern Rebud", "Eastern Redcedar"],
            "answer": "Water Oak",
            "image_path": "default.jpg"
        }
    ],
    "Common from Scientific 3": [
        {
            "question": "Toxicodendron Radicans",
            "options": ["Poison Ivy", "Eastern Rebud", "Eastern Redcedar", "American Sweetgum"],
            "answer": "Poison Ivy",
            "image_path": "default.jpg"
        },
        {
            "question": "Cercis Canadensis",
            "options": ["Eastern Rebud", "Eastern Redcedar", "American Sweetgum", "Shining Sumac"],
            "answer": "Eastern Redbud",
            "image_path": "default.jpg"
        },
        {
            "question": "Juniperus Virginiana",
            "options": ["Eastern Redcedar", "American Sweetgum", "Shining Sumac", "Red Maple"],
            "answer": "Eastern Redcedar",
            "image_path": "default.jpg"
        },
        {
            "question": "Liquidambar Styraciflua",
            "options": ["American Sweetgum", "Shining Sumac", "Red Maple", "American Mistletoe"],
            "answer": "American Sweetgum",
            "image_path": "default.jpg"
        },
        {
            "question": "Rhus Copallinum",
            "options": ["Shining Sumac", "Red Maple", "American Mistletoe", "Bald Cypress"],
            "answer": "Shining Sumac",
            "image_path": "default.jpg"
        }
    ],
    "Common from Scientific 4": [
        {
            "question": "Acer Rubrum",
            "options": ["Red Maple", "American Mistletoe", "Bald Cypress", "American Sycamore"],
            "answer": "Red Maple",
            "image_path": "default.jpg"
        },
        {
            "question": "Phoradendron Lencarpum",
            "options": ["American Mistletoe", "Bald Cypress", "American Sycamore", "Tulip Poplar"],
            "answer": "American Mistletoe",
            "image_path": "default.jpg"
        },
        {
            "question": "Taxodium Distichum",
            "options": ["Bald Cypress", "American Sycamore", "Tulip Poplar", "Black Locust"],
            "answer": "Bald Cypress",
            "image_path": "default.jpg"
        },
        {
            "question": "Platanus Occidentalis",
            "options": ["American Sycamore", "Tulip Poplar", "Black Locust", "Trumpet Creeper"],
            "answer": "American Sycamore",
            "image_path": "default.jpg"
        },
        {
            "question": "Liriodendron Tulipifera",
            "options": ["Tulip Poplar", "Black Locust", "Trumpet Creeper", "Flowering Dogwood"],
            "answer": "Tulip Poplar",
            "image_path": "default.jpg"
        },
        {
            "question": "Robinia Pseudoacacia",
            "options": ["Black Locust", "Trumpet Creeper", "Flowering Dogwood", "Bradford Pear"],
            "answer": "Black Locust",
            "image_path": "default.jpg"
        }
    ],
    "Common from Family 1": [
        {
            "question": "Bignoniaceae",
            "options": ["Trumpet Creeper", "Flowering Dogwood", "Bradford Pear", "Crepe Myrtle"],
            "answer": "Trumpet Creeper",
            "image_path": "default.jpg"
        },
        {
            "question": "Cornaceae",
            "options": ["Flowering Dogwood", "Bradford Pear", "Crepe Myrtle", "Southern Magnolia"],
            "answer": "Flowering Dogwood",
            "image_path": "default.jpg"
        },
        {
            "question": "Rosaceae",
            "options": ["Bradford Pear", "Crepe Myrtle", "Southern Magnolia", "Virginia Creeper"],
            "answer": "Bradford Pear",
            "image_path": "default.jpg"
        },
        {
            "question": "Lythraceae",
            "options": ["Crepe Myrtle", "Southern Magnolia", "Virginia Creeper", "Dogfennel"],
            "answer": "Crepe Myrtle",
            "image_path": "default.jpg"
        },
        {
            "question": "Magnoliaceae",
            "options": ["Southern Magnolia", "Virginia Creeper", "Dogfennel", "Pecan"],
            "answer": "Southern Magnolia",
            "image_path": "default.jpg"
        }
    ],
    "Common from Family 2": [
        {
            "question": "Vitaceae",
            "options": ["Virginia Creeper", "Dogfennel", "Pecan", "Black Cherry"],
            "answer": "Virginia Creeper",
            "image_path": "default.jpg"
        },
        {
            "question": "Asteraceae",
            "options": ["Dogfennel", "Pecan", "Black Cherry", "Water Oak"],
            "answer": "Dogfennel",
            "image_path": "default.jpg"
        },
        {
            "question": "Juglandaceae",
            "options": ["Pecan", "Black Cherry", "Water Oak", "Poison Ivy"],
            "answer": "Pecan",
            "image_path": "default.jpg"
        },
        {
            "question": "Rosaceae",
            "options": ["Black Cherry", "Water Oak", "Poison Ivy", "Eastern Redbud"],
            "answer": "Black Cherry",
            "image_path": "default.jpg"
        },
        {
            "question": "Fagaceae",
            "options": ["Water Oak", "Poison Ivy", "Eastern Rebud", "Eastern Redcedar"],
            "answer": "Water Oak",
            "image_path": "default.jpg"
        }
    ],
    "Common from Family 3": [
        {
            "question": "Anacardiaceae",
            "options": ["Poison Ivy", "Eastern Rebud", "Eastern Redcedar", "American Sweetgum"],
            "answer": "Poison Ivy",
            "image_path": "default.jpg"
        },
        {
            "question": "Fabaceae",
            "options": ["Eastern Rebud", "Eastern Redcedar", "American Sweetgum", "Shining Sumac"],
            "answer": "Eastern Redbud",
            "image_path": "default.jpg"
        },
        {
            "question": "Cupressaceae",
            "options": ["Eastern Redcedar", "American Sweetgum", "Shining Sumac", "Red Maple"],
            "answer": "Eastern Redcedar",
            "image_path": "default.jpg"
        },
        {
            "question": "Hamamelidaceae",
            "options": ["American Sweetgum", "Shining Sumac", "Red Maple", "American Mistletoe"],
            "answer": "American Sweetgum",
            "image_path": "default.jpg"
        },
        {
            "question": "Anacardiaceae",
            "options": ["Shining Sumac", "Red Maple", "American Mistletoe", "Bald Cypress"],
            "answer": "Shining Sumac",
            "image_path": "default.jpg"
        }
    ],
    "Common from Family 4": [
        {
            "question": "Aceraceae",
            "options": ["Red Maple", "American Mistletoe", "Bald Cypress", "American Sycamore"],
            "answer": "Red Maple",
            "image_path": "default.jpg"
        },
        {
            "question": "Santalaceae",
            "options": ["American Mistletoe", "Bald Cypress", "American Sycamore", "Tulip Poplar"],
            "answer": "American Mistletoe",
            "image_path": "default.jpg"
        },
        {
            "question": "Cupressaceae",
            "options": ["Bald Cypress", "American Sycamore", "Tulip Poplar", "Black Locust"],
            "answer": "Bald Cypress",
            "image_path": "default.jpg"
        },
        {
            "question": "Platanaceae",
            "options": ["American Sycamore", "Tulip Poplar", "Black Locust", "Trumpet Creeper"],
            "answer": "American Sycamore",
            "image_path": "default.jpg"
        },
        {
            "question": "Magnoliaceae",
            "options": ["Tulip Poplar", "Black Locust", "Trumpet Creeper", "Flowering Dogwood"],
            "answer": "Tulip Poplar",
            "image_path": "default.jpg"
        },
        {
            "question": "Fabaceae",
            "options": ["Black Locust", "Trumpet Creeper", "Flowering Dogwood", "Bradford Pear"],
            "answer": "Black Locust",
            "image_path": "default.jpg"
        }
    ]
}

class CategorySelector:
    def __init__(self, master):
        self.master = master
        master.title("Choose a Category")

        self.label = tk.Label(master, text="Select a Quiz Category:", font=("Arial", 16))
        self.label.pack(pady=20)

        for category in question_bank.keys():
            btn = tk.Button(master, text=category, font=("Arial", 14), width=20,
                            command=lambda c=category: self.start_quiz(c))
            btn.pack(pady=10)

    def start_quiz(self, category):
        self.master.destroy()
        root = tk.Tk()
        QuizApp(root, category)
        root.mainloop()

class QuizApp:
    def __init__(self, master, category):
        self.master = master
        self.master.title(f"{category} Quiz")

        self.questions = question_bank[category]
        random.shuffle(self.questions)

        self.current_question = 0
        self.score = 0

        self.image_label = tk.Label(master)
        self.image_label.pack(pady=10)

        self.question_label = tk.Label(master, text="", font=("Arial", 16), wraplength=500, justify="center")
        self.question_label.pack(pady=10)

        self.buttons = []
        for _ in range(4):
            btn = tk.Button(master, text="", font=("Arial", 14), width=25)
            btn.pack(pady=5)
            self.buttons.append(btn)

        self.next_button = tk.Button(master, text="Next", font=("Arial", 12), command=self.next_question, state=tk.DISABLED)
        self.next_button.pack(pady=10)

        self.status_label = tk.Label(master, text="", font=("Arial", 12))
        self.status_label.pack()

        self.load_question()

    def load_question(self):
        self.selected = False
        q = self.questions[self.current_question]

        # Load and display image
        try:
            img = Image.open(q["image_path"])
            img = img.resize((600, 400), Image.Resampling.LANCZOS)
            self.photo = ImageTk.PhotoImage(img)
            self.image_label.config(image=self.photo)
        except Exception as e:
            print("Error loading image:", e)
            self.image_label.config(image='', text="[Image not found]", font=("Arial", 12))

        # Set question
        self.question_label.config(text=q["question"])

        # Shuffle and display options
        options = q["options"].copy()
        random.shuffle(options)
        for idx, option in enumerate(options):
            self.buttons[idx].config(text=option, state=tk.NORMAL, bg="gray",
                                     command=lambda opt=option: self.check_answer(opt))

        self.next_button.config(state=tk.DISABLED)
        self.status_label.config(text=f"Question {self.current_question + 1} of {len(self.questions)}")

    def check_answer(self, selected_option):
        if self.selected:
            return

        self.selected = True
        correct = self.questions[self.current_question]["answer"]

        for btn in self.buttons:
            btn.config(state=tk.DISABLED)
            if btn['text'] == correct:
                btn.config(bg="green")
            elif btn['text'] == selected_option:
                btn.config(bg="red")

        if selected_option == correct:
            self.score += 1

        self.next_button.config(state=tk.NORMAL)

    def next_question(self):
        self.current_question += 1
        if self.current_question >= len(self.questions):
            self.show_result()
        else:
            self.load_question()

    def show_result(self):
        messagebox.showinfo("Quiz Complete", f"You scored {self.score} out of {len(self.questions)}!")
        self.master.destroy()
        root = tk.Tk()
        app = CategorySelector(root)
        root.mainloop()

# Start the app with category selection
if __name__ == "__main__":
    root = tk.Tk()
    app = CategorySelector(root)
    root.mainloop()
