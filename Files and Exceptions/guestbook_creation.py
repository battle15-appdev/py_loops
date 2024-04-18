""" 
This program takes the user's input and and store in a separate file
File is in the same directory

"""

filename = "responses.txt"

prompt = "List an inspiring quote: "
response = ''

while response != 'q':
    response = input(prompt)

    with open(filename, 'a') as file_object:
        file_object.write(f"\n{response}")
