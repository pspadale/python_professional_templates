"""
Project comments, Date, copyright notice and company stamp, notes.
"""

try:
    from tkinter import *
except ImportError:  # Python 2.0 Import
    import Tkinter as tkinter

from tkinter import ttk

# import yourModuleWithClass.py

# fonts list
font = {0: 'Arial 11',
        1: 'Arial 11 bold',
        2: 'Arial 16 bold',
        3: 'Arial 26 bold',
        4: 'Verdana 11',
        5: 'Verdana 11 bold',
        6: 'Verdana 16 bold',
        7: 'Verdana 26 bold',
        8: 'Tahoma 11',
        9: 'Tahoma 11 bold',
        10: 'Tahoma 16 bold',
        11: 'Tahoma 26 bold'}


class Application(object):
    """
    This class creates the tkinter objects with all interfaces. You can include other .py files with different
    classes and inherited from master which have other functionality.
    """
    def __init__(self, master):
        self.master = master

        # sample label widget on the screen.
        self.lbl_SampleLabel = ttk.Label(self.master, text="sample label widget", font=font[11])
        self.lbl_SampleLabel.pack(pady=15)


def main():
    root = Tk()
    root.geometry("600x600+300+50")  # size 600 x 600 with x offset 300 and y offset 50 from top left.
    root.title("Your App Name")
    App = Application(root)
    root.mainloop()


if __name__ == "__main__":
    main()
