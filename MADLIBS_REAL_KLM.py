# """
# Author: Luke, Kaizer, Mac
# Assignment Title: MadLibs
# Assignment Description: Create Madlib
# Due Date: 12/6
# Date Created: 11/17
# Date Last Modified: 12/6

# Data Abstraction

story1=""
story2=""
story3=""
story4=""

#Dictionaries for word storage
story_format = {}


def make_word_list(word_list, story_number):
    global story_format
    word_list = [word.strip() for word in word_list]
    if story_number == 1:
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
    if story_number == 2:
        story_format = {
            'name': word_list[0],
            'adjective1': word_list[1],
            'adjective2': word_list[2],
            'adjective3': word_list[3],
            'number1': word_list[4],
            'food': word_list[5],
            'number2': word_list[6],
            'adjective4': word_list[7],
            'adjective5': word_list[8],
            'facial_feature': word_list[9],
            'number3': word_list[10],
            'place': word_list[11],
            'number4': word_list[12]
        }

    if story_number ==3:
        story_format = {
            'verb': word_list[0],
            'adverb': word_list[1],
            'plural_creatures': word_list[2],
            'name': word_list[3],
            'adjective1': word_list[4],
            'place': word_list[5],
            'job': word_list[6],
            'sea_animal': word_list[7],
            'number': word_list[8],
            'past_tense_verb': word_list[9],
            'prefix': word_list[7][:3]
        }
    if story_number == 4:
        story_format = {
            'verb': word_list[0],
            'adverb': word_list[1],
            'plural_animals': word_list[2],
            'name': word_list[3],
            'adjective1': word_list[4],
            'job': word_list[5],
            'number': word_list[6],
            'animal': word_list[7],
            'past_tense_verb': word_list[8],
            'prefix': word_list[3][:3]
        }
    return story_format

def get_story():
    global story1
    global story2
    global story3
    global story4

    mystory = open("stories.txt")
    contents = mystory.readlines()
    mystory.close()

    story1 = contents[1:21]
    story1 = "".join(story1)

    story2 = contents[23:37]
    story2 = "".join(story2)

    story3 = contents[39:59]
    story3 = "".join(story3)

    story4 = contents[62:92]
    story4 = "".join(story4)
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




