"""
Author: Luke, Kaizer, Mac
Assignment Title: MadLibs
Assignment Description: Create Madlib
Due Date: 12/6
Date Created: 11/17
Date Last Modified: 11/17

"""
#Project Goal
#Create four different stories randomly selected using the random library
#Prompt the user for the words like normal
#Use Tkinter to display story and relating picture. (drawn by turtle?)

#Version Update 3.0
#Skeleton code is basically done, need to figure out how to add Tkinter to this
#Might make 3rd and 4th story
#TODO: remove random and have user pick story
#put stories in separate file and read them

# Data Abstraction
import tkinter as tk
status_label = None

#Dictionaries for word storage
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

#stories

# story_one = """
# The rain {verb} across the concrete jungle.
# It was {adverb} quiet — so quiet that only the footsteps of
# {plural_animals} echoed through the empty streets.
# New {name} City’s crime hour had just begun.
# Who knew what {adjective1} chaos was unfolding in this crime-soaked metropolis?
#
# But high above it all, perched on the edge of the {job} building,
# stood the city’s unlikely guardian. By day, they were billionaire company owner
# {name} Wayne… but by night, they became the {adjective1},
# the legendary: {animal}-Warrior
#
# They checked their wrist for the {prefix}-signal — there were {number} crimes
# happening across the city. Without hesitation, they {past_tense_verb} toward the
# {prefix}-mobile, heart pounding with purpose.
#
# But after a long night, even heroes have limits.
#
# They slipped into the {prefix}-cave, collapsed onto the couch,
# and spent the rest of the night watching Instagram Reels instead.
# """
#
# story_two = """
# In the magical country of {name} Kingdom, there sat a {adjective1} King on the
# {adjective2} throne in the {adjective3} tower on the Northeastern side of the first
# half of palace on the third Friday of the 2nd month of the calendar year.
#
# The King was hungry and ordered his servant to fetch him {number1} {food}s from the mess hall.
# The servant hasn’t returned for {number2} years.
#
# The King was bored and ordered the jester to entertain him.
# The jester made fun of the King's {adjective4} {adjective5} {facial_feature}, which made the King
# let out a huge chuckle and send the jester away. The jester hasn’t been seen for {number3} years.
#
# Dumbfounded by all the nonsense, the King decided to go to {place} for some fresh air.
# The King was gone for {number4} years.
# """
#
# #add these later
# story_three = """
# """
# story_four = """
# """

def get_story(number):
    mystory = open("stories.txt")
    contents = mystory.read()
    return contents

def input_words(story_selected, story_number):
    for i in story_selected.keys():
        story_selected[i] = input(f"Enter {story_selected[i]}: ")
    if story_number == 1:
        story_selected["prefix"] = story_selected["animal"][:3]
    return story_selected

def accept_input(event=None):
    user_text = textbox.get()
    print("User typed:", user_text)
    textbox.delete(0,"end")

def story_select():
    global status_label
    root = tk.Tk()
    root.title("MadLibs")
    label = tk.Label(root, text="Enter story number:", font=("Arial", 40))
    font=("Impact", 40)
    root.geometry("600x400")
    label.pack()
    textbox = tk.Text(root, width=20, height=5, bd=4, relief="ridge", font=("Arial", 40))
    textbox.pack(pady=50)
    story_number = accept_input
    root.mainloop()

    story_number = int(input("Enter story number: "))
    if story_number == 1:
        story_selected = word_types_one
        story_selected = input_words(story_selected, story_number)
        temp = get_story(story_number)
        story = temp.format(**story_selected)
    elif story_number == 2:
        story_selected = word_types_two
        story_selected = input_words(story_selected, story_number)
        temp = get_story(story_number)
        story = temp.format(**story_selected)
    elif story_number == 3:
        story_selected = word_types_three
        story_selected = input_words(story_selected, story_number)
        temp = get_story(story_number)
        story = temp.format(**story_selected)
    elif story_number == 4:
        story_selected = word_types_four
        story_selected = input_words(story_selected, story_number)
        temp = get_story(story_number)
        story = temp.format(**story_selected)

    return story

def display_story(story):
    print(story)


if __name__ =="__main__":
# Input
    story = story_select()
# Process
# Output
    display_story(story)
# Assumptions
