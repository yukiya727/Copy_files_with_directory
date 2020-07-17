import pickle
import os

# example = "This is a pickle"

pickle_out = open("str.pickle","wb")
pickle.dump(example, pickle_out)
pickle_out.close()

pickle_in = open("str.pickle", "rb")
example = pickle.load(pickle_in)

print(example)
pickle_in.close()
