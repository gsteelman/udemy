fileName = "ex.txt"
fileMode = "a"
# File opened in appened mode doesn't overwrite previous contents
file = open(fileName, fileMode)
file.write("Line 4\n")
file.close()