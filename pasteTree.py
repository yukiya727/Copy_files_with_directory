import os
import sys
import pickle
import shutil

progPath = os.path.dirname(sys.argv[0])
progPath = os.path.dirname(os.path.dirname(progPath))
pDir = progPath + "\\loc.pickle"
dst = sys.argv[-1]
if os.path.exists(pDir):
    p = open(pDir, "rb")
    temppath = pickle.load(p)
    p.close()
    os.remove(pDir)

    folder = temppath[1]
    folder = folder[len(temppath[2]):]
    dst = dst + folder

    if not os.path.exists(dst):
        os.makedirs(dst)

    cp = shutil.copy(temppath[0] ,dst)
     
    shutil.rmtree(temppath[2], True)
