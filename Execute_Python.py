
#import runpy to run Python file through HyperMesh Python window
import runpy
#import tkinter to create an open file dialog
import tkinter as tk
from tkinter import filedialog
import os


#change 1st time
root = tk.Tk()
root.withdraw()  # hide the root window
#set initial folder as Desktop
desktop_folder = os.path.join(os.environ['USERPROFILE'], 'Desktop')
#select script file
filename = filedialog.askopenfilename(initialdir=desktop_folder,
                                    title="Select Python Script",
                                    filetypes=[("Python Script", "*.py")])

with open(filename, 'r') as f:
    script = f.read()
exec(script)

#this is the second change

