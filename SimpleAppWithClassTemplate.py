"""
Project comments, Date, copyright notice and company stamp, notes.
"""

try:
    from tkinter import *
except ImportError:  # Python 2.0 Import
    import Tkinter as tkinter

from tkinter import ttk
from tkinter import messagebox
import os

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

        def donothing():
            pass

        def about():
            txt = ""
            if os.path.isfile('lic.dat'):
                with open("lic.dat", 'r') as f:
                    for line in f:
                        txt += line

            messagebox.showinfo("Sample application", "Sample application developed for testing by D Sign Design"
                                                      "\nLicense expiry date is {}".format(txt))

        def deactivate():
            # self.lic.license_remove()
            self.master.quit()

        # Menus creations
        menubar = Menu(self.master)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="New", command=donothing)
        filemenu.add_command(label="Open", command=donothing)
        filemenu.add_command(label="Save", command=donothing)
        filemenu.add_command(label="Save as...", command=donothing)
        filemenu.add_command(label="Close", command=donothing)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.master.quit)
        menubar.add_cascade(label="File", menu=filemenu)

        editmenu = Menu(menubar, tearoff=0)
        editmenu.add_command(label="Undo", command=donothing)
        editmenu.add_separator()
        editmenu.add_command(label="Cut", command=donothing)
        editmenu.add_command(label="Copy", command=donothing)
        editmenu.add_command(label="Paste", command=donothing)
        editmenu.add_command(label="Delete", command=donothing)
        editmenu.add_command(label="Select All", command=donothing)
        menubar.add_cascade(label="Edit", menu=editmenu)

        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(label="Deactivate License", command=deactivate)
        helpmenu.add_command(label="About...", command=about)
        menubar.add_cascade(label="Help", menu=helpmenu)

        self.master.config(menu=menubar)


def main():
    root = Tk()
    root.geometry("600x600+300+50")  # size 600 x 600 with x offset 300 and y offset 50 from top left.
    root.title("Your App Name")
    App = Application(root)
    root.mainloop()


if __name__ == "__main__":
    main()
