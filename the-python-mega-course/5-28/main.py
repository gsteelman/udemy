def currency_converter(currency_value, exchange_rate):
  new_currency_value = currency_value * exchange_rate
  return new_currency_value

print("Currency converter")
currency_value = float(raw_input("Enter currency value: "))
exchange_rate = float(raw_input("Enter exchange rate: "))

converted_currency = currency_converter(currency_value, exchange_rate)
print("Converted currency = %.2f" % converted_currency)