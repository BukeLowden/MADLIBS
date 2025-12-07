import tkinter as tk
from tkinter import messagebox
from MADLIBS_REAL_KLM import get_story, make_story, make_word_list

class ML_GUI:

    def __init__(self):
        #Data Abstraction

        #Stories
        story1, story2, story3, story4= get_story()

        #Colors, Fonts, Etc
        page_color = "#FFF8DE"
        story_font_style = ("Times New Roman", 12)
        font_style = ("Times New Roman", 20)

        #Story fields to organize words properly

        label_widgets = {}
        text_widgets = {}

        field1 = [
            ("v", "Verb:", 1000, 80),
            ("adv", "Adverb:", 990, 140),
            ("pla", "Plural Animal:", 950, 200),
            ("na", "Name:", 1000, 260),
            ("adj", "Adjective:", 980, 320),
            ("oc", "Occupation:", 970, 380),
            ("ani", "Animal:", 990, 440),
            ("num", "Number:", 990, 500),
            ("ptv", "Past Tense Verb:", 940, 560),
        ]

        field2 = [
            ("name", "Name:", 1000, 80),
            ("adjective1", "Adjective 1:", 970, 140),
            ("adjective2", "Adjective 2:", 970, 200),
            ("adjective3", "Adjective 3:", 970, 260),
            ("number1", "Number 1:", 980, 320),
            ("food", "Food:", 1000, 380),
            ("number2", "Number 2:", 980, 440),
            ("adjective4", "Adjective 4:", 970, 500),
            ("adjective5", "Adjective 5:", 970, 560),
            ("facial_feature", "Facial Feature:", 1315, 80),
            ("number3", "Number 3:", 1345, 140),
            ("place", "Place:", 1360, 200),
            ("number4", "Number 4:", 1345, 260),
        ]

        field3 = [
            ("verb", "Verb:", 1000, 80),
            ("adverb", "Adverb:", 990, 140),
            ("plural_creatures", "Plural Creatures:", 950, 200),
            ("name", "Name:", 1000, 260),
            ("adjective1", "Adjective:", 980, 320),
            ("place", "Place:", 990, 380),
            ("job", "Job:", 1005, 440),
            ("sea_animal", "Sea Animal:", 980, 500),
            ("number", "Number:", 990, 560),
            ("past_tense_verb", "Past Tense Verb:", 1330, 80),
        ]

        field4 = [
            ("verb", "Verb:", 1000, 80),
            ("adverb", "Adverb:", 990, 140),
            ("plural_animals", "Plural Animals:", 950, 200),
            ("name", "Name:", 1000, 260),
            ("adjective1", "Adjective:", 980, 320),
            ("job", "Job:", 1005, 380),
            ("number", "Number:", 990, 440),
            ("animal", "Animal:", 995, 500),
            ("past_tense_verb", "Past Tense Verb:", 1330, 80),

        ]

        #Functions

        def display(completed_story):
            #displays the story in a pop up window
            messagebox.showinfo(title="message", message=completed_story)

        def submit(page):
            #assigns word order based on page number
            field_order = []
            story_number = 0
            if page==page1:
                story_number = 1
                field_order = ["v", "adv", "pla", "na", "adj", "oc", "ani", "num", "ptv"]
            if page==page2:
                story_number = 2
                field_order = [
                    "name",
                    "adjective1",
                    "adjective2",
                    "adjective3",
                    "number1",
                    "food",
                    "number2",
                    "adjective4",
                    "adjective5",
                    "facial_feature",
                    "number3",
                    "place",
                    "number4"
                ]
            if page==page3:
                story_number = 3
                field_order = [
                    "verb",
                    "adverb",
                    "plural_creatures",
                    "name",
                    "adjective1",
                    "place",
                    "job",
                    "sea_animal",
                    "number",
                    "past_tense_verb"
                ]
            if page==page4:
                story_number = 4
                field_order = [
                    "verb",
                    "adverb",
                    "plural_animals",
                    "name",
                    "adjective1",
                    "job",
                    "number",
                    "animal",
                    "past_tense_verb"
                ]

            #gets all the text in the textboxes 
            word_list = [text_widgets[i].get("1.0", "end").strip() for i in field_order]

            story_format = make_word_list(word_list, story_number)
            completed_story = make_story(story_format, story_number)
            display(completed_story)

        def display_page(page):
            story = ""
            chapter_num = 0
            title_text = ""
            button_text = "Turn Page"
            if page==page1:
                story = story1
                title_text = "The Bathman"
                chapter_num = "- Chapter 1 -"
            elif page==page2:
                story = story2
                title_text = "The King"
                chapter_num = "- Chapter 2 -"
            elif page==page3:
                story= story3
                title_text = "Tidewalker"
                chapter_num = "- Chapter 3 -"
            elif page==page4:
                story=story4
                title_text = "Whispers"
                chapter_num = "- Chapter 4 -"
                button_text = "Beginning"


            chapter = tk.Label(page, text=chapter_num, font=("Times New Roman", 20), bg=page_color)
            title = tk.Label(page, text=title_text, font=("Times New Roman", 50), bg=page_color)
            page_divider = tk.Label(page, text="|", font=("Times New Roman", 60), bg=page_color)
            page_story = tk.Label(page, text=story, font=("Times New Roman", 15), bg=page_color)

            chapter.place(x=400, y=100, anchor="center")
            title.place(x=400, y=160, anchor="center")
            page_divider.place(x=800, y=500, anchor="center")
            if page==page4:
                page_story.place(x=400, y=600, anchor="center")
            else:
                page_story.place(x=400, y=500, anchor="center")

            p1_submit_button = tk.Button(page, text="Submit", font=("Times New Roman", 20), bg="White", height=2,
                                         width=30, command=lambda: submit(page))

            p1_turn_button = tk.Button(page, text=button_text, font=("Times New Roman", 20), bg="White", height=2,
                                       width=8, command=lambda: turn_page(page))

            p1_submit_button.place(x=1200, y=700, anchor="center")
            p1_turn_button.place(x=1360, y=800, anchor="center")

        def turn_page(page=0, direction=0):
            page1.forget()
            page2.forget()
            page3.forget()
            page4.forget()
            field = field1
            if page==0:
                page=page1
                field = field1
            elif page==page1:
                page=page2
                field = field2
            elif page==page2:
                page=page3
                field = field3
            elif page==page3:
                page=page4
                field = field4
            elif page==page4:
                page=page1
                field=field1

            for key, label_text, x, y in field:
                # Create label
                word_label = tk.Label(page, text=label_text, font=font_style, bg=page_color)

                word_label.place(x=x, y=y, anchor="center")
                label_widgets[key] = word_label

                # Create text box
                txt = tk.Text(page, height=1, width=10, font=font_style, bg="white")
                if x >=1315:
                    txt.place(x=1500, y=y, anchor="center")
                else:
                    txt.place(x=1110, y=y, anchor="center")
                text_widgets[key] = txt

            display_page(page)
            page.pack(fill="both", expand=True)



        #Creating the window

        self.root = tk.Tk()
        self.root.geometry("1600x1000")
        self.root.title("Madlibs")

        #pages

        page1 = tk.Frame(self.root, bg=page_color)
        page2 = tk.Frame(self.root, bg=page_color)
        page3 = tk.Frame(self.root, bg=page_color)
        page4 = tk.Frame(self.root, bg=page_color)
        turn_page()


        page1.pack(fill="both", expand=True)


        self.root.mainloop()


ML_GUI()
