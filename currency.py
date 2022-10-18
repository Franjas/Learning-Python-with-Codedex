# Create a program that asks the user for the amount they have in yuan, yen, and won and calculates the total in USD.
# codédex

cny = float(input('Enter the amount in CNY: '))
jpy = float(input('Enter the amount in JPY: '))
krw = float(input('Enter the amount in KRW: '))

amount = (cny * 0.14) + (jpy * 0.0067) + (krw * 0.00070)  # exchange rate 18/10/2022

print('The amount in USD is:', '$',amount)