import os
import re
import sys
import tempfile
from tkinter import Tk
from tkinter.filedialog import askdirectory
import shutil
import pickle

import subprocess

# Tk().withdraw()
path = askdirectory(title='Select the starting folder you want to copy from')

# src = "c:\\Users\\x'j\\Documents\\Workspace\\Copy_files_with_directory\\readme.md"
src = sys.argv[0]
# dst = "c:\\Users\\x'j\\Documents\\Workspace"
dst = askdirectory(title='Select the starting folder you want to copy from')

if not dst in src:
    sys.exit()


dstpath = os.path.dirname(dst)
srcpath = os.path.dirname(src)
copypath = srcpath[len(dstpath):]
print(copypath)

# def mkfolder():
temppath = tempfile.mkdtemp()
copypath = temppath + copypath

if not os.path.exists(copypath):
    os.makedirs(copypath)

# Copy the file to temp dir
cp = shutil.copy(src, copypath)
os.startfile(copypath)
tempdir = [cp, copypath, temppath]

p = open("loc.pickle", "wb")
pickle.dump(tempdir, p)
p.close()