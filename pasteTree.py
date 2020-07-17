import os
import sys
import pickle
import shutil


if os.path.exists("loc.pickle"):
    p = open("loc.pickle", "rb")
    temppath = pickle.load(p)
    p.close()
    os.remove("loc.pickle")

    dst = sys.argv[0]
    dst = dst + temppath[1]

    if not os.path.exists(dst):
        os.makedirs(dst)

     cp = shutil.copy(temppath[0] ,dst)
     shutil.rmtree(temppath[2])
