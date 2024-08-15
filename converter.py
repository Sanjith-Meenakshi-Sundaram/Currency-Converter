from currency_converter import CurrencyConverter
# to create a name for CurrencyRates class
C = CurrencyConverter()
# Input
amount = input("Enter the amount: ")
from_currency = input("From Currency ").upper()
to_currency = input("To Currency ").upper()
# Converting
result = C.convert(amount,from_currency, to_currency)
#result
print(result)
