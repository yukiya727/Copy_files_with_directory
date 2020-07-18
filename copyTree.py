import os
import re
import sys
import tempfile
from tkinter import Tk
from tkinter.filedialog import askdirectory
import shutil
import pickle
import subprocess


Tk().withdraw()
dst = askdirectory(title='Select the starting folder you want to copy from')
dst = dst.replace("/", "\\")

src = " ".join(sys.argv[1:])


# Check if the file is inculded in the directory selected
if not dst in src:
    sys.exit()


progPath = os.path.dirname(os.path.dirname(os.path.dirname(sys.argv[0])))
pDir = progPath + "\\loc.pickle"

if os.path.exists(pDir):
    p = open(pDir, "rb")
    tempPath = pickle.load(p)
    p.close()
    os.remove(pDir)
    shutil.rmtree(tempPath[2], True)


dstPath = os.path.dirname(dst)
srcPath = os.path.dirname(src)
copyPath = srcPath[len(dstPath):]

tempPath = tempfile.mkdtemp()
copyPath = tempPath + copyPath


# Copy the directory tree structure in a temp dir
if not os.path.exists(copyPath):
    os.makedirs(copyPath)


# Copy the file to temp dir
cp = shutil.copy(src, copyPath)

tempdir = [cp, copyPath, tempPath]

# Pickle the temp dir location
p = open(pDir, "wb")
pickle.dump(tempdir, p)
p.close()