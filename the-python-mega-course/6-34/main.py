inputFileName = "input.txt"
inputFileMode = "r"
inputFile = open(inputFileName, inputFileMode)
print(type(inputFile))

# Read entire contents of file at once into a string
content = inputFile.read()
print(type(content))
print(content)

# Reset read pointer to beginning of file
inputFile.seek(0)
# Read one line of file into a string
content = inputFile.readline()
print(type(content))
print(content)

# Reset read pointer to beginning of file
inputFile.seek(0)
# Read entire contents of file at once into a list of strings
content = inputFile.readlines()
print(type(content))
print(content)
# Strip \n from all lines. This is a for comprehension.
content = [line.rstrip("\n") for line in content]
print(type(content))
print(content)

inputFile.close()