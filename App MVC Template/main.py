import view

"""
App name and app object launched from this file. 
icons and license check etc. Can be a part of this file. This app folder will have 4 files. This one should be launched 
for main application. This is based on MVC architecture. The template from the stack-overflow for the multi frame view 
is being modified in this MVC architecture. 

control.py  -> which is imported here will have main business logic code, objects, classes. 
view.py -> Will have all interface elements and related objects, classes. 
model.py -> will have all the code related database or data elements. 
"""

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


if __name__ == "__main__":
    app = view.TemplateApp()
    app.mainloop()
