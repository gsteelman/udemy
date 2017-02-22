r"""
This is the docstring. The r preceding it makes python interpret this as a "raw string" 
So things like \n do not insert a newline, but instead actually show on the printout.

It can be printed by executing print(__doc__)

Or by importing this module via "import main" then print(main.__doc__)
"""

fileName = "example.txt"
fileMode = "w"

# Create empty file 
def createFile():
  """
  This method creates an empty file.

  This docstring can be printed by doing createFile.__doc__
  """
  with open(fileName, fileMode) as file:
    file.write("") # Write nothing to the file.