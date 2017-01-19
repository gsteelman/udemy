def currency_converter(currency_value, exchange_rate):
  new_currency_value = currency_value * exchange_rate
  return new_currency_value

converted_currency = currency_converter(10, 1.5)
print(converted_currency)