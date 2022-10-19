# Create a program that can answer any Yes or No questions with a different fortune/advice each time it executes.
# Codédex

import random

questions = ['Am I good at programming?',
             'Will the world be better every day?',
             'Will I buy a house and a car soon?',
             'Is Codédex very good for learning?',
             'Is consuming a lot of calories good for me?',
             'Is exercising good for me?',
             'Will I meet Codédex friends?',
             'Will I get a job soon?',
             'Will I be rich?']

magic_8_ball = ['Yes, definitely.',
           'It is decidedly so.',
           'Without a doubt.',
           'Reply hazy, try again.',
           'Ask again later.',
           'Better not tell you now.',
           'My sources say no.',
           'Outlook not so good.',
           'Very doubtful.']

print(random.choice(questions))
print(random.choice(magic_8_ball))