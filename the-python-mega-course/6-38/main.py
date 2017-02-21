fileName = "ex.txt"
fileMode = "a+"

# Open a new block where "file" is opened and closed automatically after close of block.
# Slightly more readable for smaller blocks dealing with the file.
with open(fileName, fileMode) as file:
  file.seek(0)
  # content is available outside the scope of the with block.
  content = file.readlines()
  file.write("Line 6\n")

print(content)