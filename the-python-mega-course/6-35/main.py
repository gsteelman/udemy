outputFileName = "output.txt"
outputFileMode = "w"
# Opening with "w" mode is an overwrite.
outputFile = open(outputFileName, outputFileMode)
outputFile.write("Line 1")
outputFile.write("Line 2")
# Changes to file aren't saved until file handle is closed
outputFile.close()

outputFile = open(outputFileName, outputFileMode)
lines = ["Line 1", "Line 2", "Line 3"]
for line in lines:
  outputFile.write(line + "\n")
outputFile.close()