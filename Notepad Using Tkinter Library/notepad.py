from tkinter import *
from tkinter.filedialog import *

class Notepad:
    root = Tk()
    root.title("Designed By Abdulrahman - Notepad")
    root.geometry("700x400")
    
    # Create a Text widget for the main body of the notepad
    text = Text(root, wrap=WORD)
    text.pack(expand=YES, fill=BOTH)
    
    # Create a Scrollbar and associate it with the Text widget
    scrollbar = Scrollbar(text)
    scrollbar.pack(side=RIGHT, fill=Y)
    text.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=text.yview)
    
    
    
    #Define functions for the menu commands
    
    #new_file
    def new_file(self):
        self.root.title=("Designed By Abdulrahman - Notepad")
        self.text.delete(1.0,END)
        
        
    #open_file
    def open_file(self):
        file = askopenfilename(defaultextension=".txt", filetypes=[("Text Documents", "*.txt"), ("All files", "*.*")])
        
        if file:
            self.root.title(f"{file} - Notepad")
            self.text.delete(1.0, END)
            with open(file, "r") as f:
                self.text.insert(INSERT, f.read())
    
    #save_file
    def save_file(self):
        file = asksaveasfilename(defaultextension=".txt", filetypes=[("Text Documents", "*.txt"), ("All Files", "*.*")])
        
        if file:
            with open(file, "w") as f:
                f.write(self.text.get(1.0, END))
            self.root.title(f"{file} - Notepad")
            
            
    def exit_notepad(self):
        self.root.destroy()
        
    def __init__(self):
        # Create the menu bar
        menu_bar = Menu(self.root)
        self.root.config(menu=menu_bar)
        
        # Create the file menu
        file_menu = Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_command(label="Open...", command = self.open_file)
        file_menu.add_command(label="Save As...", command = self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command = self.exit_notepad)
        menu_bar.add_cascade(label="File", menu=file_menu)
        
        #Create the Edit menu
        edit_menu = Menu(menu_bar, tearoff=0)
        edit_menu.add_command(label="Undo")
        edit_menu.add_separator()
        edit_menu.add_command(label="Cut")
        edit_menu.add_command(label="Copy")
        edit_menu.add_command(label="Paste")
        edit_menu.add_command(label="Delete")
        edit_menu.add_separator()
        edit_menu.add_command(label="Select All")
        menu_bar.add_cascade(label="Edit", menu=edit_menu)
        
        #Create the Help menu
        help_menu = Menu(menu_bar, tearoff=0)
        help_menu.add_command(label="About")
        menu_bar.add_cascade(label="Help", menu=help_menu)
        
        self.root.mainloop()
        
Notepad()
             
        
        
    
    
    