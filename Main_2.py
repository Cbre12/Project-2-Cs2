from GUI_2 import Gui
from tkinter import *

def main():
# This main creates the GUI window.
 
    window = Tk()
    window.title("Dog Food Calculator")
    window.geometry('300x300')
    window.resizable(False, False)
    Gui(window)
    window.mainloop()

if __name__ == "__main__":
    main()