import tkinter as tk  # python 3
from tkinter import font  as tkfont  # python 3

from tkinter import ttk
# import Tkinter as tk     # python 2
# import tkFont as tkfont  # python 2

"""
from :
https://stackoverflow.com/questions/32864610/understanding-parent-and-controller-in-tkinter-init

Roughly speaking, the original code1 attempted to use a pseudo-MVC (model, view and controller) architecture. 
Though without the "model" part -- there was just a "view" (some frames) and a "controller" (the main application). 
Hence, the reference to a controller object. The original code was actually written to show how to "stack" frames, 
so it's MVC implementation is very shallow and under-documented since that wasn't the point of the example.

To answer your specific questions:

self represents the current object. This is a common first parameter for any method of a class. 
As you suggested, it's similar to Java's this.

parent represents a widget to act as the parent of the current object. 
All widgets in tkinter except the root window require a parent (sometimes also called a master)

controller represents some other object that is designed to act as a common point of interaction for several pages of widgets. 
It is an attempt to decouple the pages. That is to say, each page doesn't need to know about the other pages. 
If it wants to interact with another page, such as causing it to be visible, it can ask the controller to make it visible.

You asked "There is a function already defined called show_frame, 
but why is the controller being used to call this function?" Notice that show_frame is defined in a separate class, 
in this case the main program class. It is not defined in the other classes. For the other classes to be able to call it, 
they must call it on an instance of the main class. That instance is named controller in the context of these other classes. 
"""
"""
Date : 10/08/2020
Code modified or rather added to have menus to main window for additional functionality. This can be commented out if 
not required. But certainly do useful when you want to use 'save', 'save as' and exit commands etc. 

Pravin Padale
D Sign design
"""

font_list = {0: 'Arial 11', 1: 'Arial 11 bold', 2: 'Arial 16 bold',
             3: 'Arial 26 bold', 4: 'Verdana 11', 5: 'Verdana 11 bold',
             6: 'Verdana 16 bold', 7: 'Verdana 26 bold', 8: 'Tahoma 11',
             9: 'Tahoma 11 bold', 10: 'Tahoma 16 bold', 11: 'Tahoma 26 bold'}


class TemplateApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # Main Page title on the main frame.
        main_title = tk.Label(self, text="App Heading", font=font_list[3])
        main_title.pack(side="top", fill="x")

        def donothing():
            pass

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # Definitions of menubar ====================================================
        menubar = tk.Menu(self)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="New", command=donothing)
        filemenu.add_command(label="Open", command=donothing)
        filemenu.add_command(label="Save", command=donothing)
        filemenu.add_command(label="Save as...", command=donothing)
        filemenu.add_command(label="Close", command=donothing)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.quit)
        menubar.add_cascade(label="File", menu=filemenu)

        editmenu = tk.Menu(menubar, tearoff=0)
        editmenu.add_command(label="Undo", command=donothing)
        editmenu.add_separator()
        editmenu.add_command(label="Cut", command=donothing)
        editmenu.add_command(label="Copy", command=donothing)
        editmenu.add_command(label="Paste", command=donothing)
        editmenu.add_command(label="Delete", command=donothing)
        editmenu.add_command(label="Select All", command=donothing)
        menubar.add_cascade(label="Edit", menu=editmenu)

        helpmenu = tk.Menu(menubar, tearoff=0)
        helpmenu.add_command(label="Deactivate License", command=donothing)
        helpmenu.add_command(label="About...", command=donothing)
        menubar.add_cascade(label="Help", menu=helpmenu)

        self.config(menu=menubar)

        # End of menubar ==============================================================

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is the start page", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Go to Page One",
                            command=lambda: controller.show_frame("PageOne"))
        button2 = tk.Button(self, text="Go to Page Two",
                            command=lambda: controller.show_frame("PageTwo"))
        button1.pack()
        button2.pack()


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 1", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 2", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


if __name__ == "__main__":
    app = TemplateApp()
    app.title("Your App Name")
    app.state("zoomed")
    app.mainloop()
