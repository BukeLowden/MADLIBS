# """
# Author: Luke, Kaizer, Mac
# Assignment Title: MadLibs
# Assignment Description: Create Madlib
# Due Date: 12/6
# Date Created: 11/17
# Date Last Modified: 12/5

#As of recent:
#Rewrote some code to make it cleaner so its just the functions we need
#Need story 3 and 4, might make 5
#Need get_story function debug, creates 3 empty lines instead of 1


# Data Abstraction

story1=""
story2=""
story3=""
story4=""

#Dictionaries for word storage
story_format = {}

#Will use this later
# word_format_2 = {
#     'name': 'a name',
#     'adjective1': 'an adjective',
#     'adjective2': 'another adjective',
#     'adjective3': 'an adjective ending in -est',
#     'number1': 'a number',
#     'food': 'a type of food (singular)',
#     'number2': 'another number',
#     'adjective4': 'an adjective',
#     'adjective5': 'another adjective',
#     'facial_feature': 'a facial feature (e.g. nose, beard)',
#     'number3': 'another number',
#     'place': 'a place',
#     'number4': 'another number'
# }
"""
word_types_sea_third = {
    'verb': 'a verb (present tense)',
    'adverb': 'an adverb',
    'plural_creatures': 'a plural sea creature',
    'name': 'a name',
    'adjective1': 'an adjective',
    'place': 'an underwater location',
    'job': 'a job/profession',
    'sea_animal': 'a sea animal (singular)',
    'prefix': 'a short prefix (like aqua, fish, sea)',
    'number': 'a number',
    'past_tense_verb': 'a past-tense verb'
}
"""


def make_word_list(word_list, id):
    global story_format
    if id == "something":
        story_format = {
            'verb': word_list[0],
            'adverb': word_list[1],
            'plural_animals': word_list[2],
            'name': word_list[3],
            'adjective1': word_list[4],
            'job': word_list[5],
            'animal': word_list[6],
            'number': word_list[7],
            'past_tense_verb': word_list[8],
            'prefix': word_list[6][:3]
        }

    return story_format

def get_story():
    global story1
    global story2
    global story3
    global story4

    f = open("stories.txt")
    contents = f.readlines()
    f.close()

    story1 = "".join(contents[0:17]).rstrip()
    story2 = "".join(contents[17:34]).rstrip()

    return story1, story2, story3, story4


def make_story(selected_words, story_number):

    story=""
    if story_number == 1:
        story = story1.format(**selected_words)
    elif story_number == 2:
        story = story2.format(**selected_words)
    elif story_number == 3:
        story = story3.format(**selected_words)
    elif story_number == 4:
        story = story4.format(**selected_words)
    return story


