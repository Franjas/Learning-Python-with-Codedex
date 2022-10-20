# Write a program that asks the user some questions using int() and places them into one of the Houses based on their answers:
#Codédex


Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0

q1 = int(input('Do you like Dawn or Dusk?\n1)Dawn\n2)Dusk\n'))

if q1 == 1:
    Gryffindor += 1
    Ravenclaw += 1
elif q1 == 2:
    Hufflepuff += 1
    Slytherin *= 1
else:
    print('Wrong input.')


q2 = int(input('When I’m dead, I want people to remember me as:\n1)The Good\n2)The Great\n3)The Wise\n4)The Bold\n'))

if q2 == 1:
    Hufflepuff += 1
elif q2 == 2:
    Slytherin += 1
elif q2 == 3:
    Ravenclaw += 1
elif q2 == 4:
    Gryffindor += 1
else:
    print('Wrong input.')
    

q3 = int(input('Which kind of instrument most pleases your ear?\n1)The violin\n2)The trumpet\n3)The piano\n4)The drum\n'))

if q3 == 1:
    Slytherin += 1
elif q3 == 2:
    Hufflepuff += 1
elif q3 == 3:
    Ravenclaw += 1
elif q3 == 4:
    Gryffindor += 1
else:
    print('Wrong input.')

print('Gryffindor:', Gryffindor)
print('Ravenclaw:', Ravenclaw)
print('Hufflepuff:', Hufflepuff)
print('Slytherin:', Slytherin)