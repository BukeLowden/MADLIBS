import tkinter as tk
from MADLIBS_REAL_KLM import get_story, make_story, make_word_list

class ML_GUI:

    def __init__(self):
        #Data Abstraction
        #Stories
        story1, story2 = get_story()
        story_list = [story1, story2]

        #Colors, Fonts, Etc
        page_color = "#FFF8DE"
        story_font_style = ("Times New Roman", 12)
        font_style = ("Times New Roman", 20)

        #Creating the window
        print(story_list[0])

        self.root = tk.Tk()
        self.root.geometry("1600x1000")
        self.root.title("Madlibs")

        #Pages, might make cover page

        page1 = tk.Frame(self.root, bg=page_color)
        page2 = tk.Frame(self.root, bg=page_color)
        page3 = tk.Frame(self.root, bg=page_color)
        page4 = tk.Frame(self.root, bg=page_color)

        #First Page Gizmos
        chapter1 = tk.Label(page1, text="- Chapter One -", font=("Times New Roman", 20), bg=page_color, fg="black")
        chapter1.place(x=400,y=100, anchor="center")
        title1 = tk.Label(page1, text="The Bathman", font=("Times New Roman", 50), bg=page_color, fg="black")
        title1.place(x=400, y=160, anchor="center")
        page_divider = tk.Label(page1, text="|", font=("Times New Roman", 60), bg=page_color)
        page_divider.place(x=800,y=500, anchor="center")

        #find if you can make buttons have dimentions, or be different shapes
        p1_submit_button = tk.Button(page1, text="Submit", font=("Times New Roman", 50), bg=page_color,fg="green")
        p1_submit_button.place(x=1200, y=700, anchor="center")
        # story_text1 = tk.Label(page1, text=story1, font=font_style, bg=page_color)
        # story_text1.place(x=400, y=600, anchor="center")

        #First Page Word Inputs, any ways to make this cleaner?
        # Goal = list the words and have text box for each individual word
        # user presses button to receive all words and either put into list or dict
        # call make story function to put words into the story
        p1_v = tk.Label(page1, text="Verb:", font=font_style, bg=page_color, fg="black")
        p1_adv = tk.Label(page1, text="Adverb:", font=font_style, bg=page_color, fg="black")
        p1_pla = tk.Label(page1, text="Plural Animal:", font=font_style, bg=page_color, fg="black")
        p1_na = tk.Label(page1, text="Name:", font=font_style, bg=page_color, fg="black")
        p1_adj = tk.Label(page1, text="Adjective:", font=font_style, bg=page_color, fg="black")
        p1_oc = tk.Label(page1, text="Occupation:", font=font_style, bg=page_color, fg="black")
        p1_ani = tk.Label(page1, text="Animal:", font=font_style, bg=page_color, fg="black")
        p1_num = tk.Label(page1, text="Number:", font=font_style, bg=page_color, fg="black")
        p1_ptv = tk.Label(page1, text="Past Tense Verb:", font=font_style, bg=page_color, fg="black")

        p1_v.place(x=1000, y=80, anchor="center")
        p1_adv.place(x=986, y=140, anchor="center")
        p1_pla.place(x=950, y=200, anchor="center")
        p1_na.place(x=995, y=260, anchor="center")
        p1_adj.place(x=980, y=320, anchor="center")
        p1_oc.place(x=970, y=380, anchor="center")
        p1_ani.place(x=990, y=440, anchor="center")
        p1_num.place(x=985, y=500, anchor="center")
        p1_ptv.place(x=940, y=560, anchor="center")
        page1.pack(fill="both", expand=True)

        v_box = tk.Text(page1, height=1, width=10, font=font_style, bg=page_color)
        adv_box = tk.Text(page1, height=1, width=10, font=font_style, bg=page_color)
        pla_box = tk.Text(page1, height=1, width=10, font=font_style, bg=page_color)
        na_box = tk.Text(page1, height=1, width=10, font=font_style, bg=page_color)
        adj_box = tk.Text(page1, height=1, width=10, font=font_style, bg=page_color)
        oc_box = tk.Text(page1, height=1, width=10, font=font_style, bg=page_color)
        ani_box = tk.Text(page1, height=1, width=10, font=font_style, bg=page_color)
        num_box = tk.Text(page1, height=1, width=10, font=font_style, bg=page_color)
        ptv_box = tk.Text(page1, height=1, width=10, font=font_style, bg=page_color)

        v_box.place(x=1110, y=80, anchor="center")
        adv_box.place(x=1110, y=140, anchor="center")
        pla_box.place(x=1110, y=200, anchor="center")
        na_box.place(x=1110, y=260, anchor="center")
        adj_box.place(x=1110, y=320, anchor="center")
        oc_box.place(x=1110, y=380, anchor="center")
        ani_box.place(x=1110, y=440, anchor="center")
        num_box.place(x=1110, y=500, anchor="center")
        ptv_box.place(x=1110, y=560, anchor="center")


        self.root.mainloop()


#make turn page function
#make submit function (command that activates make_word_list)

ML_GUI()
