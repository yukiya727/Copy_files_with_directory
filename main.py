from tkinter import Tk
from tkinter.filedialog import askdirectory
# shows dialog box and return the path


Tk().withdraw()
path = askdirectory(title='Select the starting folder you want to copy from')
print(path)
