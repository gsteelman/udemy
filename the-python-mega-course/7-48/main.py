"""
Concatenate files from one dir into one file.
"""

import datetime
import glob
import os

def constructGlob(dir, extension):
  """
  Construct a glob pattern to match files of the given extension in the given directory.
  """
  globPattern =  dir + "/*." + extension
  return globPattern

def getInputFilePaths(dir, extension):
  """
  Get a list of the file paths in the directory with a matching extension.
  """
  globPattern = constructGlob(dir, extension)
  #print("globPattern = " + globPattern)
  inputFilePaths = glob.glob(globPattern)
  return inputFilePaths

def getOutputFilePath(dir):
  """
  Generate an output file path in the given directory.
  """
  now = datetime.datetime.now()
  fileName = now.strftime("%Y-%m-%d-%H-%M-%S-%f")
  outputFilePath = os.getcwd() + "/" + fileName + ".txt"
  return outputFilePath

def main():
  """
  The driver.
  """
  inputDir = os.getcwd() + "/Sample-Files"
  inputFilesExtension = "txt"
  inputFileMode = "r"
  outputDir = os.getcwd()
  outputFileMode = "w"

  inputFilePaths = getInputFilePaths(inputDir, inputFilesExtension)
  print(inputFilePaths)
  outputFilePath = getOutputFilePath(outputDir)
  print(outputFilePath)

  # Open output file, open each input file, read lines one at a time into output file.
  with open(outputFilePath, outputFileMode) as outputFile:
    for inputFilePath in inputFilePaths:
      with open(inputFilePath, inputFileMode) as inputFile:
        for line in inputFile:
          if (line.endswith("\n") != True):
            line = line + "\n"
          # NB: print adds a newline, so these show on console with two newlines, but have only one in output file.
          print(line)
          outputFile.write(line)

  # Open output file, print it to the screen for confirmation of contents easily.
  with open(outputFilePath, inputFileMode) as outputFile:
    for line in outputFile:
      print(line)

main()