# Internal imports
from Unit import Unit
from Comp import Comp
import helperLib
from tft_constants import *

# External imports
from tkinter import *
import tkinter.messagebox

### MAIN LOOP ###

def main() :

    ### INITIALIZE VARIABLES ###

    c = Comp([ZED, ZOE, JINX])

    ### BUTTON FUNCTIONS ###

    def on_unit_btn_clicked(action : str) :
        # Get unit input
        unit_str = unit_entry.get().upper()
        unit_list = [unit for unit in SET_8_UNITS if unit.name.upper() == unit_str]

        if (len(unit_list) > 0) :
            # unit exists
            unit = unit_list[0]
            if (action=="ADD") :
                c.add_unit(unit)
            else :
                c.remove_unit(unit)
            
            comp_text.delete("1.0", END)

            # print text with colors
            comp_string_list = c.get_comp_string_list()
            comp_text.insert(END, comp_string_list[0] + "\n")
            for line in comp_string_list[1:] :
                comp_text.insert(END, line[0], line[1], "\n")

            # Update suggestions
            suggestions = c.find_suggestions([k for k in c.synergies_count if c.synergies_count[k]!=0])
            suggestions_text.delete("1.0", END)
            suggestions_text.insert(INSERT, suggestions)
        
        else :
            # unit doesn't exist
            tkinter.messagebox.showerror("Invalid unit !", 'Unit doesn\'t exist, please try again !')

    def on_reset_btn_clicked() :
        while (c.units) :
            c.remove_unit(c.units[-1])
        comp_text.delete("1.0", END)
        suggestions_text.delete("1.0", END)



    ## GUI ELEMENTS ###

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
    add_btn = Button(buttons_frame, text="Add unit", width=10, height=2, command=lambda action="ADD" : on_unit_btn_clicked(action))
    remove_btn = Button(buttons_frame, text="Remove unit", width=10, height=2, command=lambda action="REMOVE" : on_unit_btn_clicked(action))
    reset_btn = Button(buttons_frame, text="Reset comp", width=10, height=2, command=on_reset_btn_clicked)

    # Layout buttons
    add_btn.grid(row=0, column=0, padx=50)
    remove_btn.grid(row=0, column=1, padx=50)
    reset_btn.grid(row=0, column=2, padx=50)

    # Create unit entry
    unit_label = Label(unit_frame, text="Unit : ")
    unit_entry = Entry(unit_frame)

    # Layout unit entry
    unit_label.grid(row=0, column=0)
    unit_entry.grid(row=0, column=1)

    # Create comp text area
    comp_text = Text(comp_frame, height=15)
    comp_string_list = c.get_comp_string_list()
    comp_text.insert(END, comp_string_list[0] + "\n")
    for line in comp_string_list[1:] :
        comp_text.insert(END, line[0], line[1], "\n")

    # Layout comp text area
    comp_text.grid(row=0, column=0, padx=10, pady=10)

    # Configure comp text area colors
    comp_text.tag_configure("Gray", foreground="gray")
    comp_text.tag_configure("Green", foreground="green")
    comp_text.tag_configure("Orange", foreground="orange")
    comp_text.tag_configure("Purple", foreground="purple")
    comp_text.tag_configure("Cyan", foreground="cyan")
    comp_text.tag_configure("Red", foreground="red")

    # Create suggestions text
    suggestions_label = Label(suggestions_frame, text="Suggestions : ")
    suggestions_text = Text(suggestions_frame, height=5)
    # placeholder
    suggestions_text.insert(INSERT, c.find_suggestions([k for k in c.synergies_count if c.synergies_count[k]!=0]))

    # Layout suggestions text
    suggestions_label.grid(row=0, column=0, padx=10)
    suggestions_text.grid(row=0, column=1, padx=10)

    # Main layout
    unit_frame.grid(row=0, padx=20, pady=20)
    buttons_frame.grid(row=1, padx=20, pady=20)
    comp_frame.grid(row=2, padx=20, pady=20)
    suggestions_frame.grid(row=3, padx=20, pady=20)

    win.mainloop()



if __name__ == "__main__" :
    main()