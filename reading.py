# Create a program that stores the following items in a books list:

    # 'Zero to One'
    # 'The Lean Startup'
    # 'The Mom Test'
    # 'Made to Stick'
    # 'Life in Code'

# Suppose we want to add one more book to the list: 'Zero to Sold'. Can you use a list method to do so?
# Codédex

books = ['Zero to One', 'The Lean Startup', 'The Mom Test',
         'Made to Stick', 'Life in Code']

# Suppose we want to add one more book to the list: 'Zero to Sold'. Can you use a list method to do so?
books.append('Zero to Sold')

# Let’s say we finished reading 'Zero to One' and 'The Lean Startup'. Can you use the .remove() method to remove one and the .pop() method to remove the other?
books.remove('Zero to One')
books.pop(0)
print(books)