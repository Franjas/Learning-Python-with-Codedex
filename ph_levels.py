# Create a program that checks whether a pH level is basic, acidic, or neutral.

# First, create a variable called ph and ask the user for a value between 0 and 14.

# Write an if, elif, else statement that:

#    If ph is greater than 7, output "Basic".
#    If ph is less than 7, output "Acidic".
#    Else, output "Neutral".
# Codédex

ph = int(input('Enter a value between 0 and 14: '))

if ph > 7:
    print('Its ph level is Basic')
    
elif ph < 7:
    print('Its ph level is Acidic')

else:
    print('Its ph level is Neutral')