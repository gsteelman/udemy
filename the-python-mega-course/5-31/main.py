def celsiusToFahrenheit(degreesCelsius):
  lowerBound = -273.15
  if degreesCelsius < lowerBound:
    return "Error, degreesCelsius must be > " + str(lowerBound)
  else:
    return (degreesCelsius * 9 / 5.0) + 32

# temperatures in C to convert to F
temperatures = [10, -20, -289, 100]

for temperature in temperatures:
  fahrenheit = celsiusToFahrenheit(temperature)
  print(fahrenheit)