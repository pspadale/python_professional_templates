from tkinter import *
from tkinter import ttk
# import yourModuleWithClass.py


class Application(object):
    """
    This class creates the tkinter objects with all interfaces. You can include other .py files with different
    classes and inherited from master which have other functionality.
    """
    def __init__(self, master):
        self.master = master

        self.lbl_SampleLabel = ttk.Label(self.master, text="sample label widget", font="Arial 16 bold")
        self.lbl_SampleLabel.pack(pady=15)


def main():
    root = Tk()
    App = Application(root)
    root.title("Your App Name")
    root.geometry("600x600+300+50")        # size 600 x 600 with x offset 300 and y offset 50 from top left.
    root.mainloop()


if __name__ == "__main__":
    main()
