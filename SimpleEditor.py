#Imported libraries
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import os

#Global variable
file_path = ""

#Button Functions
#New file creation
def new_file():
    global file_path
    file_path = ""
    textbox.delete(1.0, END)

#Open an existing file with a dialog box
def open_file():
    global file_path
    
    textbox.delete(1.0, END)
    filename = filedialog.askopenfilename()
    file_path = os.path.abspath(filename)
    text = open(file_path, 'r')
    content = text.read()
    textbox.insert(END, content)
    return file_path

#Overwrite a file that exisits
def save():
    global file_path
    if os.path.exists(file_path) == False:
        return save_as()
    else:
        save_text = str(textbox.get(1.0, "end-1c"))
        with open(file_path, "w") as f:
            f.write(save_text)
    
#Save with new path
def save_as():
    global file_path
    filename = filedialog.asksaveasfilename()
    file_path = os.path.abspath(filename)
    print(file_path)
    save_file = textbox.get(1.0, "end-1c")
    with open(file_path, "w") as f:
        f.write(save_file)

#Creating the root window
root = Tk()
root.title("COSC110 - a5 {}".format(file_path))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

#Build a frame to hold all widgets
frame = ttk.Frame(root, padding ="4")
frame.grid(column=0, row=0, sticky=(N, S, E, W))
for i in range(4):
    frame.columnconfigure(i, weight=1)
    frame.rowconfigure(i, weight=1)

#Build all widgets
textbox = Text(frame)
new = ttk.Button(frame, text="New", command=new_file)
open_btn = ttk.Button(frame, text="Open", command=open_file)
save_btn = ttk.Button(frame, text="Save", command=save)
save_as_btn = ttk.Button(frame, text="Save As", command=save_as)
text_scrollbar = ttk.Scrollbar(frame, orient=VERTICAL, command=textbox.yview)

#Place widgets and configure
textbox.grid(column=0, columnspan=4, row=0, sticky=(N, S, E, W))
textbox["yscrollcommand"] = text_scrollbar.set
textbox["wrap"] = "word"
new.grid(column=0, row=3, sticky=(E, W), padx=2)
open_btn.grid(column=1, row=3, sticky=(E, W), padx=2)
save_btn.grid(column=2, row=3, sticky=(E, W), padx=2)
save_as_btn.grid(column=3, row=3, sticky=(E, W), padx=2)
text_scrollbar.grid(column=5, row=0, rowspan=3, sticky=(N, S))

root.mainloop()
