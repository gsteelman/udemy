import datetime

# Poll time from the system
currentTime = datetime.datetime.now()
print(type(currentTime))
print(currentTime)

# Create a datetime
previousTime = datetime.datetime(2017, 02, 11, 14, 30, 00, 500)
print(previousTime)
difference = currentTime - previousTime
print(difference)
print(difference.days)
print(difference.total_seconds())

futureTime = currentTime + datetime.timedelta(days = 2, minutes = 30)
print(futureTime)

import time
times = []
for itr in range(5):
  times.append(datetime.datetime.now())
  # sleep for approximately 1 second
  time.sleep(1)

for time in times:
  print(time)

fileName = str(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f") + ".txt")
fileMode = "w"

# Create empty file 
def createFile():
  """
  This method creates an empty file.

  This docstring can be printed by doing createFile.__doc__
  """
  with open(fileName, fileMode) as file:
    file.write("") # Write nothing to the file.

createFile()

