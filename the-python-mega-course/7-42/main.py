# "module" for interacting with underlying OS
import os

# python3 doens't require specifying a path.
currDirListing = os.listdir(os.getcwd())

print(currDirListing)
print(os.__file__)

# "library" for interacting with XML. 
# Libraries are dirs, whereas modules are single files. The __init__.py(c) 
# file in a lib directory is executed at import time, usually to import 
# everything useful for you.
import xml

help(xml)

# "packages" are 3rd party libs for things like biology, astronomy, etc.
# pip is a "library" which comes with python.
# pip install glob2, etc.