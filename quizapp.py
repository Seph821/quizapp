import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random

# Questions grouped by categories
question_bank = {
    "Life Span": [
        {
            "question": "A plant that completes its life cycle in one growing season",
            "options": ["Annual", "Biennial", "Prennial"],
            "answer": "Annual",
            "image_path": "cat.jpg"
        },
        {
            "question": "A plant that completes its life cycle in two growing seasons",
            "options": ["Annual", "Biennial", "Prennial"],
            "answer": "Biennial",
            "image_path": "cat.jpg"
        },
        {
            "question": "Any plant that lives for more than two growing seasons",
            "options": ["Annual", "Biennial", "Prennial"],
            "answer": "Prennial",
            "image_path": "cat.jpg"
        }

    ],
    "Plant Habit": [
        {
            "question": "A plant with little or no above-ground prennial woody tissue",
            "options": ["Herb", "Subshrub", "Shrub", "Tree"],
            "answer": "Herb",
            "image_path": "cat.jpg"
        },
        {
            "question": "A plant having the stature of a shrub but not completely woody",
            "options": ["Subshrub", "Shrub", "Tree", "Succulent"],
            "answer": "Subshrub",
            "image_path": "cat.jpg"
        },
        {
            "question": "A woody perennial plant of comparatively low stature with one to many relative slender trunks from near its base",
            "options": ["Shrub", "Tree", "Succulent", "Vine"],
            "answer": "Shrub",
            "image_path": "cat.jpg"
        },
        {
            "question": "A large woody plant with one to several relatively massive trunks and an elevated crown",
            "options": ["Tree", "Succulent", "Vine", "Liana"],
            "answer": "Tree",
            "image_path": "cat.jpg"
        },
        {
            "question": "A plant with thick, usually soft, watery leaves and/or stems",
            "options": ["Tree", "Succulent", "Vine", "Liana"],
            "answer": "Succulent",
            "image_path": "cat.jpg"
        },
        {
            "question": "Climbing plant with herbaceous stems",
            "options": ["Tree", "Succulent", "Vine", "Liana"],
            "answer": "Vine",
            "image_path": "cat.jpg"
        },
        {
            "question": "Climbing plant with woody stems",
            "options": ["Tree", "Succulent", "Vine", "Liana"],
            "answer": "Liana",
            "image_path": "cat.jpg"
        }

    ],
    "Root Types": [
        {
            "question": "A central main root that descends vertically:; it is larger than any branch roots",
            "options": ["Tap Root", "Fibrous Root", "Adventitious Root"],
            "answer": "Tap Root",
            "image_path": "mars.jpg"
        },
        {
            "question": "A thin root arising from another root or from stem tissue",
            "options": ["Tap Root", "Fibrous Root", "Adventitious Root"],
            "answer": "Fibrous Root",
            "image_path": "mars.jpg"
        },
        {
            "question": "A root that originates from stem or leaf tissue rather than from the interior of another root",
            "options": ["Tap Root", "Fibrous Root", "Adventitious Root"],
            "answer": "Adventitious Root",
            "image_path": "mars.jpg"
        }

    ],
    "Stem Types": [
        {
            "question": "Prostrate to erect, above-ground stems.  These are the most commonly encountered types of stems",
            "options": ["Aerial Stems", "Rhizome", "Stolon", "Bulb"],
            "answer": "Aerial Stems",
            "image_path": "cat.jpg"
        },
        {
            "question": "An underground, horizontal stem that spreads and perennates a plant",
            "options": ["Rhizome", "Stolon", "Bulb", "Corm"],
            "answer": "Rhizome",
            "image_path": "cat.jpg"
        },
        {
            "question": "A horizontal stem at or just above the surface of the ground that gives rise to a new plant at its tip or from axillary branches.  It may bend to the ground and surface.",
            "options": ["Stolon", "Bulb", "Corm", "Tuber"],
            "answer": "Stolon",
            "image_path": "cat.jpg"
        },
        {
            "question": "A thickened, short vertical stem axis with large, fleshy storage leaves attacked; usually borne below ground.",
            "options": ["Stolon", "Bulb", "Corm", "Tuber"],
            "answer": "Bulb",
            "image_path": "cat.jpg"
        },
        {
            "question": "A solid, erect, enlarged underground stem with leaves absent or dry and scalelike; usually borne below ground",
            "options": ["Stolon", "Bulb", "Corm", "Tuber"],
            "answer": "Corm",
            "image_path": "cat.jpg"
        },
        {
            "question": "A solid enlarged, horizontal, shortened, stem, usually borne below ground.",
            "options": ["Stolon", "Bulb", "Corm", "Tuber"],
            "answer": "Tuber",
            "image_path": "cat.jpg"
        }
        ],
    "Plant Structures": [
        {
            "question": "A",
            "options": ["Terminal bud", "Internode", "Lateral bud", "Node"],
            "answer": "Terminal bud",
            "image_path": "plant_structures.jpg"
        },
        {
            "question": "B",
            "options": ["Internode", "Lateral bud", "Node", "Leaf Scar"],
            "answer": "Internode",
            "image_path": "plant_structures.jpg"
        },
        {
            "question": "C",
            "options": ["Lateral bud", "Node", "Leaf scar", "Lenticel"],
            "answer": "Lateral bud",
            "image_path": "plant_structures.jpg"
        },
        {
            "question": "D",
            "options": ["Node", "Leaf scar", "Lenticel", "Terminal bud scale scars"],
            "answer": "Node",
            "image_path": "plant_structures.jpg"
        },
        {
            "question": "E",
            "options": ["Leaf scar", "Lenticel", "Terminal bud scale scars", "Blade"],
            "answer": "Leaf scar",
            "image_path": "plant_structures.jpg"
        },
        {
            "question": "F",
            "options": ["Lenticel", "Terminal bud scale scars", "Blade", "Petiole"],
            "answer": "Lenticel",
            "image_path": "plant_structures.jpg"
        },
        {
            "question": "G",
            "options": ["Terminal bud scale scars", "Blade", "Petiole", "Stipule"],
            "answer": "Terminal bud scale scars",
            "image_path": "plant_structures.jpg"
        },
        {
            "question": "H",
            "options": ["Blade", "Petiole", "Stipule", "Stipule scar"],
            "answer": "Blade",
            "image_path": "plant_structures.jpg"
        },
        {
            "question": "I",
            "options": ["Blade", "Stipule", "Stipule scar", "Petiole"],
            "answer": "Petiole",
            "image_path": "plant_structures.jpg"
        },
        {
            "question": "J",
            "options": ["Stipule", "Stipule scar", "Petiole", "Stipules"],
            "answer": "Stipule",
            "image_path": "plant_structures.jpg"
        },
        {
            "question": "K",
            "options": ["Stipule", "Stipule scar", "Petiole", "Stipules"],
            "answer": "Stipule scar",
            "image_path": "plant_structures.jpg"
        },
        {
            "question": "L",
            "options": ["Stipule", "Stipule scar", "Petiole", "Stipules"],
            "answer": "Petiole",
            "image_path": "plant_structures.jpg"
        },
        {
            "question": "M",
            "options": ["Stipule", "Stipule scar", "Petiole", "Stipules"],
            "answer": "Stipules",
            "image_path": "plant_structures.jpg"
        }

    ],
    "Leaf Shapes": [
        {
            "question": "A",
            "options": ["Needlelike", "Scalelike", "Linear", "Oblong"],
            "answer": "Needlelike",
            "image_path": "leaf_shapes.jpg"
        },
        {
            "question": "B",
            "options": ["Scalelike", "Linear", "Oblong", "Lanceolate"],
            "answer": "Scalelike",
            "image_path": "leaf_shapes.jpg"
        },
        {
            "question": "C",
            "options": ["Linear", "Oblong", "Lanceolate", "Eliptic"],
            "answer": "Linear",
            "image_path": "leaf_shapes.jpg"
        },
        {
            "question": "D",
            "options": ["Oblong", "Lanceolate", "Eliptic", "Oblanceolate"],
            "answer": "Oblong",
            "image_path": "leaf_shapes.jpg"
        },
        {
            "question": "E",
            "options": ["Lanceolate", "Eliptic", "Oblanceolate", "Ovate"],
            "answer": "Lanceolate",
            "image_path": "leaf_shapes.jpg"
        },
        {
            "question": "F",
            "options": ["Eliptic", "Oblanceolate", "Ovate", "Broadly eliptic"],
            "answer": "Eliptic",
            "image_path": "leaf_shapes.jpg"
        },
        {
            "question": "G",
            "options": ["Oblanceolate", "Ovate", "Broadly eliptic", "Obovate"],
            "answer": "Oblanceolate",
            "image_path": "leaf_shapes.jpg"
        },
        {
            "question": "H",
            "options": ["Ovate", "Broadly eliptic", "Obovate", "Orbicular"],
            "answer": "Ovate",
            "image_path": "leaf_shapes.jpg"
        },
        {
            "question": "I",
            "options": ["Broadly eliptic", "Obovate", "Orbicular", "Reniform"],
            "answer": "Broadly eliptic",
            "image_path": "leaf_shapes.jpg"
        },
        {
            "question": "J",
            "options": ["Broadly eliptic", "Obovate", "Orbicular", "Reniform"],
            "answer": "Obovate",
            "image_path": "leaf_shapes.jpg"
        },
        {
            "question": "K",
            "options": ["Broadly eliptic", "Obovate", "Orbicular", "Reniform"],
            "answer": "Orbicular",
            "image_path": "leaf_shapes.jpg"
        },
        {
            "question": "L",
            "options": ["Broadly eliptic", "Obovate", "Orbicular", "Reniform"],
            "answer": "Reniform",
            "image_path": "leaf_shapes.jpg"
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
