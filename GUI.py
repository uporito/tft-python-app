from tkinter import *
import tkinter.messagebox

win=Tk()
win.title('TFT Comp Maker')
win.geometry('800x600')

# configure the grid
# win.rowconfigure(0, weight=1)
# win.rowconfigure(1, weight=1)
# win.rowconfigure(2, weight=1)
# win.rowconfigure(3, weight=1)

def msg(m) :
    tkinter.messagebox.showinfo('Message', m)

# Create main containers
buttons_frame = Frame(win)
unit_frame = Frame(win)
comp_frame = LabelFrame(win, text="My Comp")
suggestions_frame = Frame(win)

# Create buttons
add_btn = Button(buttons_frame, text="Add unit", width=10, height=2, command=lambda m="Adding unit" : msg(m))
remove_btn = Button(buttons_frame, text="Remove unit", width=10, height=2, command=lambda m="Removing unit" : msg(m))
suggest_btn = Button(buttons_frame, text="Suggest unit", width=10, height=2, command=lambda m="Suggesting unit" : msg(m))

# Layout buttons
add_btn.grid(row=0, column=0, padx=50)
remove_btn.grid(row=0, column=1, padx=50)
suggest_btn.grid(row=0, column=2, padx=50)

# Create unit entry
unit_label = Label(unit_frame, text="Unit : ")
unit_entry = Entry(unit_frame)

# Layout unit entry
unit_label.grid(row=0, column=0)
unit_entry.grid(row=0, column=1)

# Create comp text area
comp_text = Text(comp_frame, height=15)
comp_text.insert(INSERT,
    """
    (3) Star Guardian
    (2) Gadgeteen
    (2) Ox Force
    (2) Mascot
    (2) Spellslinger
    (1) Aegis
    (1) Defender
    (1) Hacker
    (1) Heart
    (1) Prankster
    """
)

# Layout comp text area
comp_text.grid(row=0, column=0, padx=10, pady=10)

# Create suggestions text
suggestions_label = Label(suggestions_frame, text="Suggestions : ")
suggestions_text = Text(suggestions_frame, height=2)
suggestions_text.insert(INSERT,
    "{'Ekko': 2, 'Vi': 1, 'Leona': 1, 'Leblanc': 1, 'Zed': 1, 'Lee Sin': 1, 'Sona': 1, 'Soraka': 1, 'Syndra': 1, 'Jinx': 1}"    
)

# Layout suggestions text
suggestions_label.grid(row=0, column=0, padx=10)
suggestions_text.grid(row=0, column=1, padx=10)

# Main layout
buttons_frame.grid(row=0, padx=20, pady=20)
unit_frame.grid(row=1, padx=20, pady=20)
comp_frame.grid(row=2, padx=20, pady=20)
suggestions_frame.grid(row=3, padx=20, pady=20)


win.mainloop()