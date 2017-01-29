def celsiusToFahrenheit(degreesCelsius):
  lowerBound = -273.15
  if degreesCelsius < lowerBound:
    return "Error, degreesCelsius must be > " + str(lowerBound)
  else:
    return (degreesCelsius * 9 / 5.0) + 32

print(celsiusToFahrenheit(-10))
print(celsiusToFahrenheit(0))
print(celsiusToFahrenheit(20))
print(celsiusToFahrenheit(100))
print(celsiusToFahrenheit(-300))