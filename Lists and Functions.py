things = ["mozzarella", "cinderella", "salmonella"]
print(things)

>>['mozzarella', 'cinderella', 'salmonella']

things = ["mozzarella", "cinderella", "salmonella"]
things[1] = things[1].capitalize()
print(things)

>>['mozzarella', 'Cinderella', 'salmonella']

things = ["mozzarella", "cinderella", "salmonella"]
things[0] = things[0].upper()
print(things)

>>['MOZZARELLA', 'cinderella', 'salmonella']

things = ["mozzarella", "cinderella", "salmonella"]
del things[2]
print(things)

>>['mozzarella', 'cinderella']

def good():
    return ['Harry', 'Ron', 'Hermione']

# Call the function and print the result
print(good())

>>['Harry', 'Ron', 'Hermione']

def get_odds():
    for number in range(10):
        if number % 2 != 0:
            yield number

# Find and print the third odd number
count = 0
for odd in get_odds():
    count += 1
    if count == 3:
        print(odd)
        break
>> 5
