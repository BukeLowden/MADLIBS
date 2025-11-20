# Data Abstraction
import tkinter as tk

# Dictionaries for word storage
word_types_one = {
    'verb': 'a verb',
    'adverb': 'an adverb',
    'plural_animals': 'a plural animal',
    'name': 'a name',
    'adjective1': 'an adjective',
    'job': 'a job title',
    'animal': 'an animal (singular)',
    'number': 'a number',
    'past_tense_verb': 'a past-tense verb'
}

word_types_two = {
    'name': 'a name',
    'adjective1': 'an adjective',
    'adjective2': 'another adjective',
    'adjective3': 'an adjective ending in -est',
    'number1': 'a number',
    'food': 'a type of food (singular)',
    'number2': 'another number',
    'adjective4': 'an adjective',
    'adjective5': 'another adjective',
    'facial_feature': 'a facial feature (e.g. nose, beard)',
    'number3': 'another number',
    'place': 'a place',
    'number4': 'another number'
}

word_types_three = {}
word_types_four = {}

# --- Story templates with blanks ---

story_one = """
The rain {verb} across the concrete jungle.
It was {adverb} quiet — so quiet that only the footsteps of
{plural_animals} echoed through the empty streets.
New {name} City’s crime hour had just begun.
Who knew what {adjective1} chaos was unfolding in this crime-soaked metropolis?

But high above it all, perched on the edge of the {job} building,
stood the city’s unlikely guardian. By day, they were billionaire company owner
{name} Wayne… but by night, they became the {adjective1},
the legendary: {animal}-Warrior

They checked their wrist for the {prefix}-signal — there were {number} crimes
happening across the city. Without hesitation, they {past_tense_verb} toward the
{prefix}-mobile, heart pounding with purpose.

But after a long night, even heroes have limits.

They slipped into the {prefix}-cave, collapsed onto the couch,
and spent the rest of the night watching Instagram Reels instead.
"""

story_two = """
In the magical country of {name} Kingdom, there sat a {adjective1} King on the
{adjective2} throne in the {adjective3} tower on the Northeastern side of the first
half of palace on the third Friday of the 2nd month of the calendar year.

The King was hungry and ordered his servant to fetch him {number1} {food}s from the mess hall.
The servant hasn’t returned for {number2} years.

The King was bored and ordered the jester to entertain him.
The jester made fun of the King's {adjective4} {adjective5} {facial_feature}, which made the King
let out a huge chuckle and send the jester away. The jester hasn’t been seen for {number3} years.

Dumbfounded by all the nonsense, the King decided to go to {place} for some fresh air.
The King was gone for {number4} years.
"""

story_three = """
Story 3 coming soon...
"""

story_four = """
Story 4 coming soon...
"""

story_templates = {
    1: story_one,
    2: story_two,
    3: story_three,
    4: story_four
}

word_types = {
    1: word_types_one,
    2: word_types_two,
    3: word_types_three,
    4: word_types_four
}

# ---------------- Tkinter UI ---------------- #

entries = {}  # maps placeholder key -> Entry widget


def on_story_change(*args):
    """Update the story template and input fields when the selected story changes."""
    # Get chosen story number (as int)
    try:
        story_number = int(story_var.get())
    except ValueError:
        return

    template = story_templates[story_number]

    # Show the original script with blanks
    template_text.config(state="normal")
    template_text.delete("1.0", "end")
    template_text.insert("1.0", template)
    template_text.config(state="disabled")

    # Clear old inputs
    for widget in inputs_frame.winfo_children():
        widget.destroy()
    entries.clear()

    # Build new inputs for this story
    prompts = word_types[story_number]
    row = 0
    for key, prompt in prompts.items():
        lbl = tk.Label(inputs_frame, text=prompt + ":", anchor="e")
        ent = tk.Entry(inputs_frame, width=25)
        lbl.grid(row=row, column=0, sticky="e", padx=5, pady=2)
        ent.grid(row=row, column=1, sticky="w", padx=5, pady=2)
        entries[key] = ent
        row += 1


def fill_story():
    """Collect inputs, fill in the blanks, and display the completed story."""
    try:
        story_number = int(story_var.get())
    except ValueError:
        return

    template = story_templates[story_number]
    prompts = word_types[story_number]

    # Get user words
    values = {}
    for key in prompts.keys():
        values[key] = entries[key].get()

    # Special rule for story 1: prefix is first 3 letters of animal
    if story_number == 1:
        animal = values.get("animal", "")
        values["prefix"] = animal[:3]

    try:
        completed = template.format(**values)
    except Exception as e:
        completed = f"Error filling story: {e}\nMake sure all blanks have a word."

    # Show completed story
    output_text.config(state="normal")
    output_text.delete("1.0", "end")
    output_text.insert("1.0", completed)
    output_text.config(state="disabled")


# --- Main Window ---

root = tk.Tk()
root.title("Mad Libs - Single Window")
root.geometry("900x700")

# Story selector (still in same window)
top_frame = tk.Frame(root)
top_frame.pack(fill="x", padx=10, pady=10)

story_label = tk.Label(top_frame, text="Choose a story (1–4):", font=("Arial", 12))
story_label.pack(side="left")

story_var = tk.StringVar(value="1")
story_dropdown = tk.OptionMenu(top_frame, story_var, "1", "2", "3", "4")
story_dropdown.pack(side="left", padx=10)

# Story template with blanks
template_label = tk.Label(root, text="Original Story Template (with blanks):",
                          font=("Arial", 11, "bold"))
template_label.pack(anchor="w", padx=10)

template_text = tk.Text(root, width=100, height=10, wrap="word",
                        state="disabled", bd=2, relief="sunken")
template_text.pack(fill="x", padx=10, pady=5)

# Inputs (same window)
inputs_label = tk.Label(root, text="Enter your words here:",
                        font=("Arial", 11, "bold"))
inputs_label.pack(anchor="w", padx=10, pady=(10, 0))

inputs_frame = tk.Frame(root)
inputs_frame.pack(fill="x", padx=10, pady=5)

# Button to fill in blanks
button_frame = tk.Frame(root)
button_frame.pack(pady=10)
fill_button = tk.Button(button_frame, text="Fill in the Story!",
                        font=("Arial", 12, "bold"), command=fill_story)
fill_button.pack()

# Completed story output (same window)
output_label = tk.Label(root, text="Completed Story:",
                        font=("Arial", 11, "bold"))
output_label.pack(anchor="w", padx=10)

output_text = tk.Text(root, width=100, height=10, wrap="word",
                      state="disabled", bd=2, relief="sunken")
output_text.pack(fill="both", expand=True, padx=10, pady=(0, 10))

# When story changes, update template + inputs in THIS window
story_var.trace_add("write", on_story_change)
on_story_change()  # initialize with story 1

root.mainloop()
