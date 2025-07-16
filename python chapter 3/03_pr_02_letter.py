letter = '''  Dear<|NAME|>
Greetings from ABC coding house.
I am happy to tell you about your selection.
you are selected!
Have a great day ahead!
thanks and regards.
BILL
Date : <|DATE|>'''
name = input("enter your name\n")
date = input("enter date\n")
letter = letter.replace("<|NAME|>", name)
letter = letter.replace("<|DATE|>", date)
print(letter)