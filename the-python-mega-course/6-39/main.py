temperatures = [10, -20, -289, 100]

# Convert a Celsius temperature to a Fahrenheit
def celsiusToFahrenheit(degreesCelsius):
  lowerBound = -273.15
  if degreesCelsius < lowerBound:
    return float("-inf")
  else:
    return float((degreesCelsius * 9 / 5.0) + 32)

# Open output file
fileName = "fahrenheitTemperatures.txt"
fileMode = "w"
with open(fileName, fileMode) as file:
  # Convert each temperature, ensure it isn't an error, then write to file.
  for temperature in temperatures:
    degreesFahrenheit = celsiusToFahrenheit(temperature)
    if degreesFahrenheit != float("-inf"):
      file.write(str(degreesFahrenheit) + "\n")
