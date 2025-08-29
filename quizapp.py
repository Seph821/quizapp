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
            "image_path": "default.jpg"
        },
        {
            "question": "A plant that completes its life cycle in two growing seasons",
            "options": ["Annual", "Biennial", "Prennial"],
            "answer": "Biennial",
            "image_path": "default.jpg"
        },
        {
            "question": "Any plant that lives for more than two growing seasons",
            "options": ["Annual", "Biennial", "Prennial"],
            "answer": "Prennial",
            "image_path": "default.jpg"
        }

    ],
    "Plant Habit": [
        {
            "question": "A plant with little or no above-ground prennial woody tissue",
            "options": ["Herb", "Subshrub", "Shrub", "Tree"],
            "answer": "Herb",
            "image_path": "default.jpg"
        },
        {
            "question": "A plant having the stature of a shrub but not completely woody",
            "options": ["Subshrub", "Shrub", "Tree", "Succulent"],
            "answer": "Subshrub",
            "image_path": "default.jpg"
        },
        {
            "question": "A woody perennial plant of comparatively low stature with one to many relative slender trunks from near its base",
            "options": ["Shrub", "Tree", "Succulent", "Vine"],
            "answer": "Shrub",
            "image_path": "default.jpg"
        },
        {
            "question": "A large woody plant with one to several relatively massive trunks and an elevated crown",
            "options": ["Tree", "Succulent", "Vine", "Liana"],
            "answer": "Tree",
            "image_path": "default.jpg"
        },
        {
            "question": "A plant with thick, usually soft, watery leaves and/or stems",
            "options": ["Tree", "Succulent", "Vine", "Liana"],
            "answer": "Succulent",
            "image_path": "default.jpg"
        },
        {
            "question": "Climbing plant with herbaceous stems",
            "options": ["Tree", "Succulent", "Vine", "Liana"],
            "answer": "Vine",
            "image_path": "default.jpg"
        },
        {
            "question": "Climbing plant with woody stems",
            "options": ["Tree", "Succulent", "Vine", "Liana"],
            "answer": "Liana",
            "image_path": "default.jpg"
        }

    ],
    "Root Types": [
        {
            "question": "A central main root that descends vertically:; it is larger than any branch roots",
            "options": ["Tap Root", "Fibrous Root", "Adventitious Root"],
            "answer": "Tap Root",
            "image_path": "default.jpg"
        },
        {
            "question": "A thin root arising from another root or from stem tissue",
            "options": ["Tap Root", "Fibrous Root", "Adventitious Root"],
            "answer": "Fibrous Root",
            "image_path": "default.jpg"
        },
        {
            "question": "A root that originates from stem or leaf tissue rather than from the interior of another root",
            "options": ["Tap Root", "Fibrous Root", "Adventitious Root"],
            "answer": "Adventitious Root",
            "image_path": "default.jpg"
        }

    ],
    "Stem Types": [
        {
            "question": "Prostrate to erect, above-ground stems.  These are the most commonly encountered types of stems",
            "options": ["Aerial Stems", "Rhizome", "Stolon", "Bulb"],
            "answer": "Aerial Stems",
            "image_path": "default.jpg"
        },
        {
            "question": "An underground, horizontal stem that spreads and perennates a plant",
            "options": ["Rhizome", "Stolon", "Bulb", "Corm"],
            "answer": "Rhizome",
            "image_path": "default.jpg"
        },
        {
            "question": "A horizontal stem at or just above the surface of the ground that gives rise to a new plant at its tip or from axillary branches.  It may bend to the ground and surface.",
            "options": ["Stolon", "Bulb", "Corm", "Tuber"],
            "answer": "Stolon",
            "image_path": "default.jpg"
        },
        {
            "question": "A thickened, short vertical stem axis with large, fleshy storage leaves attacked; usually borne below ground.",
            "options": ["Stolon", "Bulb", "Corm", "Tuber"],
            "answer": "Bulb",
            "image_path": "default.jpg"
        },
        {
            "question": "A solid, erect, enlarged underground stem with leaves absent or dry and scalelike; usually borne below ground",
            "options": ["Stolon", "Bulb", "Corm", "Tuber"],
            "answer": "Corm",
            "image_path": "default.jpg"
        },
        {
            "question": "A solid enlarged, horizontal, shortened, stem, usually borne below ground.",
            "options": ["Stolon", "Bulb", "Corm", "Tuber"],
            "answer": "Tuber",
            "image_path": "default.jpg"
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
    ],
    "Leaf Apices": [
        {
            "question": "A",
            "options": ["Acute", "Acuminate", "Obtuse", "Rounded"],
            "answer": "Acute",
            "image_path": "leaf_apices.jpg"
        },
        {
            "question": "B",
            "options": ["Acuminate", "Obtuse", "Rounded", "Mucronate"],
            "answer": "Acuminate",
            "image_path": "leaf_apices.jpg"
        },
        {
            "question": "C",
            "options": ["Obtuse", "Rounded", "Mucronate", "Emarginate"],
            "answer": "Obtuse",
            "image_path": "leaf_apices.jpg"
        },
        {
            "question": "D",
            "options": ["Rounded", "Mucronate", "Emarginate", "Truncate"],
            "answer": "Rounded",
            "image_path": "leaf_apices.jpg"
        },
        {
            "question": "E",
            "options": ["Rounded", "Mucronate", "Emarginate", "Truncate"],
            "answer": "Mucronate",
            "image_path": "leaf_apices.jpg"
        },
        {
            "question": "F",
            "options": ["Rounded", "Mucronate", "Emarginate", "Truncate"],
            "answer": "Emarginate",
            "image_path": "leaf_apices.jpg"
        },
        {
            "question": "G",
            "options": ["Rounded", "Mucronate", "Emarginate", "Truncate"],
            "answer": "Truncate",
            "image_path": "leaf_apices.jpg"
        }
    ],
    "Leaf Bases": [
        {
            "question": "A",
            "options": ["Acute", "Acuminate", "Obtuse", "Rounded"],
            "answer": "Acute",
            "image_path": "leaf_bases.jpg"
        },
        {
            "question": "B",
            "options": ["Acuminate", "Obtuse", "Rounded", "Truncate"],
            "answer": "Acuminate",
            "image_path": "leaf_bases.jpg"
        },
        {
            "question": "C",
            "options": ["Obtuse", "Rounded", "Truncate", "Cordate"],
            "answer": "Obtuse",
            "image_path": "leaf_bases.jpg"
        },
        {
            "question": "D",
            "options": ["Rounded", "Truncate", "Cordate", "Oblique"],
            "answer": "Rounded",
            "image_path": "leaf_bases.jpg"
        },
        {
            "question": "E",
            "options": ["Truncate", "Cordate", "Oblique", "Hastate"],
            "answer": "Truncate",
            "image_path": "leaf_bases.jpg"
        },
        {
            "question": "F",
            "options": ["Cordate", "Oblique", "Hastate", "Sagittate"],
            "answer": "Cordate",
            "image_path": "leaf_bases.jpg"
        },
        {
            "question": "G",
            "options": ["Oblique", "Hastate", "Sagittate", "Peltate"],
            "answer": "Oblique",
            "image_path": "leaf_bases.jpg"
        },
        {
            "question": "H",
            "options": ["Oblique", "Hastate", "Sagittate", "Peltate"],
            "answer": "Hastate",
            "image_path": "leaf_bases.jpg"
        },
        {
            "question": "I",
            "options": ["Oblique", "Hastate", "Sagittate", "Peltate"],
            "answer": "Sagittate",
            "image_path": "leaf_bases.jpg"
        },
        {
            "question": "J",
            "options": ["Oblique", "Hastate", "Sagittate", "Peltate"],
            "answer": "Peltate",
            "image_path": "leaf_bases.jpg"
        }
    ],
    "Leaf Margins": [
        {
            "question": "A",
            "options": ["Entire", "Crenate", "Crenulate", "Serrate"],
            "answer": "Entire",
            "image_path": "leaf_margins.jpg"
        },
        {
            "question": "B",
            "options": ["Crenate", "Crenulate", "Serrate", "Serrulate"],
            "answer": "Crenate",
            "image_path": "leaf_margins.jpg"
        },
        {
            "question": "C",
            "options": ["Crenulate", "Serrate", "Serrulate", "Doubly serrate"],
            "answer": "Crenulate",
            "image_path": "leaf_margins.jpg"
        },
        {
            "question": "D",
            "options": ["Serrate", "Serrulate", "Doubly serrate", "Denate"],
            "answer": "Serrate",
            "image_path": "leaf_margins.jpg"
        },
        {
            "question": "E",
            "options": ["Serrulate", "Doubly serrate", "Denate", "Denticulate"],
            "answer": "Serrulate",
            "image_path": "leaf_margins.jpg"
        },
        {
            "question": "F",
            "options": ["Doubly serrate", "Denate", "Denticulate", "Pinnately lobed"],
            "answer": "Doubly serrate",
            "image_path": "leaf_margins.jpg"
        },
        {
            "question": "G",
            "options": ["Denate", "Denticulate", "Pinnately lobed", "Palmately lobed"],
            "answer": "Denate",
            "image_path": "leaf_margins.jpg"
        },
        {
            "question": "H",
            "options": ["Denticulate", "Pinnately lobed", "Palmately lobed", "Plane"],
            "answer": "Denticulate",
            "image_path": "leaf_margins.jpg"
        },
        {
            "question": "I",
            "options": ["Pinnately lobed", "Palmately lobed", "Plane", "Involute"],
            "answer": "Pinnately lobed",
            "image_path": "leaf_margins.jpg"
        },
        {
            "question": "J",
            "options": ["Palmately lobed", "Plane", "Involute", "Revolute"],
            "answer": "Palmately lobed",
            "image_path": "leaf_margins.jpg"
        },
        {
            "question": "K",
            "options": ["Plane", "Involute", "Revolute", "Undulate"],
            "answer": "Plane",
            "image_path": "leaf_margins.jpg"
        },
        {
            "question": "L",
            "options": ["Plane", "Involute", "Revolute", "Undulate"],
            "answer": "Involute",
            "image_path": "leaf_margins.jpg"
        },
        {
            "question": "M",
            "options": ["Plane", "Involute", "Revolute", "Undulate"],
            "answer": "Revolute",
            "image_path": "leaf_margins.jpg"
        },
        {
            "question": "N",
            "options": ["Plane", "Involute", "Revolute", "Undulate"],
            "answer": "Undulate",
            "image_path": "leaf_margins.jpg"
        }
    ],
    "Common Name from Scientific": [
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
            "options": ["Flowering Dogwood", "Bradford Pear", "Crepe Myrtle", "Southern Magnolia"],
            "answer": "Bradford Pear",
            "image_path": "default.jpg"
        },
        {
            "question": "Lagerstroemia sp.",
            "options": ["Flowering Dogwood", "Bradford Pear", "Crepe Myrtle", "Southern Magnolia"],
            "answer": "Crepe Myrtle",
            "image_path": "default.jpg"
        },
        {
            "question": "Magnolia grandiflora",
            "options": ["Flowering Dogwood", "Bradford Pear", "Crepe Myrtle", "Southern Magnolia"],
            "answer": "Southern Magnolia",
            "image_path": "default.jpg"
        }
    ],
    "Family (Latin) from Scientific": [
        {
            "question": "Campsis radicans",
            "options": ["Bignoniaceae", "Cornaceae", "Rosaceae", "Lythraceae"],
            "answer": "Bignoniaceae",
            "image_path": "default.jpg"
        },
        {
            "question": "Cornus florida",
            "options": ["Cornaceae", "Rosaceae", "Lythraceae", "Magnoliaceae"],
            "answer": "Cornaceae",
            "image_path": "default.jpg"
        },
        {
            "question": "Pyrus calleryana",
            "options": ["Cornaceae", "Rosaceae", "Lythraceae", "Magnoliaceae"],
            "answer": "Rosaceae",
            "image_path": "default.jpg"
        },
        {
            "question": "Lagerstroemia sp.",
            "options": ["Cornaceae", "Rosaceae", "Lythraceae", "Magnoliaceae"],
            "answer": "Lythraceae",
            "image_path": "default.jpg"
        },
        {
            "question": "Magnolia grandiflora",
            "options": ["Cornaceae", "Rosaceae", "Lythraceae", "Magnoliaceae"],
            "answer": "Magnoliaceae",
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
