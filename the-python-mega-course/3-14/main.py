def celsiusToFahrenheit(degreesCelsius):
  return (degreesCelsius * 9 / 5.0) + 32

def fahrenheitToCelsius(degreesFahrenheit):
  return (degreesFahrenheit - 32) * 5 / 9.0

print(celsiusToFahrenheit(-10))
print(celsiusToFahrenheit(0))
print(celsiusToFahrenheit(20))
print(celsiusToFahrenheit(100))

print(fahrenheitToCelsius(-15))
print(fahrenheitToCelsius(0))
print(fahrenheitToCelsius(32))
print(fahrenheitToCelsius(73))
print(fahrenheitToCelsius(100))

print(celsiusToFahrenheit(fahrenheitToCelsius(32)))
print(fahrenheitToCelsius(celsiusToFahrenheit(32)))