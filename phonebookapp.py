# phonebook_dict = {
#   'Alice': '703-493-1834',
#   'Bob': '857-384-1234',
#   'Elizabeth': '484-584-2923'
# }

# #prints Elizabeths phone number
# print phonebook_dict['Elizabeth']
# #adds kareem's phone number
# phonebook_dict['Kareem'] = '938-281-1234'
# print phonebook_dict
# #delets Alice's phone number
# del phonebook_dict['Alice']
# print phonebook_dict
# #changes Bob's phone number
# phonebook_dict['Bob'] = '985-234-1234'
# print phonebook_dict
# # prints all the phone numbers
# print phonebook_dict.values()


# ramit = {
#   'name': 'Ramit',
#   'email': 'ramit@gmail.com',
#   'interests': ['movies', 'tennis'],
#   'friends': [
#     {
#       'name': 'Jasmine',
#       'email': 'jasmine@yahoo.com',
#       'interests': ['photography', 'tennis']
#     },
#     {
#       'name': 'Jan',
#       'email': 'jan@hotmail.com',
#       'interests': ['movies', 'tv']
#     }
#   ]
# }

# # Write a python expression that gets the email address of Ramit.
# print ramit['email']
# # Write a python expression that gets the first of Ramit's interests.
# print ramit['interests'][0]
# # Write a python expression that gets the email address of Jasmine.
# print ramit['friends'][0]['email']
# # Write a python expression that gets the second of Jan's two interests.
# print ramit['friends'][0]['interests'][1]



word_input = str(raw_input("Please enter a word: "))
counter = {}
for letter in word_input:
  if letter in counter:
    counter[letter] += 1
  else:
    counter[letter] = 1

print counter

