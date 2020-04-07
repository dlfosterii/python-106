#hotel app

hotel = {
    '101' : '',
    '102' : '',
    '103' : '',
    '104' : '',
    '105' : '',

    }

guest_info = {
    'occupant name' : "James",
    'phone number' : '770-555-3235',
    'prepaid?' : False
}

guest_info = {
    'occupant name' : "James",
    'phone number' : '770-555-3235',
    'prepaid?' : False
}
menu = '''

1. Check-in new guest
2. Check-out guest
3. Check room availability

'''

print('Guest check-in/check-out system')


guest_info['occupant name'] = input('Guest name? ')
guest_info['phone number'] = input('Phone number? ')
guest_info['prepaid?'] = input('Has guest prepaid for their room? ')


room_assign = input('Assign to which room? ')
hotel[room_assign] = guest_info
print(hotel)

#this will prompt for phone and assign to the key 'phone number for new_guest



# Exercise instructions...

# Small: Single hotel


# The goal of the small exercise is to get practice with the syntax for querying and manipulating the data in a single, nested dictionary.

# Write functions to:

# - is_vacant(which_hotel, '101')
#     - check if a room is occupied
# - check_in('101', guest_dictionary)
#     - assign a person to a room
# - check_out('101')
#     - returns the person dictionary in that room

# Please look back at any notes or slides for how to perform any of these actions.

# Medium: three hotels

# First, create a list of hotel dictionaries. They should contain at least 3 identical dictionaries (like the one in the example above).

# Create a while True loop to show the following menu:


# 1. Print hotel room status
# 2. Check in customer
# 3. Check out customer
# 4. Quit

# - When printing, show all rooms for all hotels and the name of the occupant, if there is one.
# - When checking a customer in, make sure to choose a hotel as well as a room.
# - Do not let a customer check into an occupied room.
# - If the room is unoccupied, prompt for each piece of information (name, cell, etc.)
# - upon check out, print out whether or not the customer has paid

# ```

# Medium: add/remove hotels

# Add more options to your main menu.

# Provide options to open a new hotel or close an existing hotel.



### GIVEN CODE BELOW HERE USE AS REFERENCE

# #hotel app
# hotel = {
#     '101': '',
#     '102': '',
#     '103': {
#         'occupant_name': 'Darlene',
#         'phone_number': 123456,
#         'has_prepaid': False    
#     },
#     '104': '',
#     '105': '',
# }
# elliot = {
#     'occupant_name': 'Elliot',
#     'phone_number': 8675309,
#     'has_prepaid': True
# }
# # guest is "checking in"
# hotel['101'] = elliot
# # customer = {}
# # name = input('What is the name of the guest? ')
# # customer['name'] = name
# # hotel['104'] = customer
# # Printing the room status
# for room_number in hotel.keys():
#     # The room_number variable will be a 
#     # string, like '101' or '103'
#     if hotel[room_number] == '':
#         print(f'{room_number} is vacant')
#     else:
#         print(f'{room_number} is occupied by {hotel[room_number]["occupant_name"]}')
# # For any one room, you should store:
# # - occupant name
# # - phone number
# # - has prepaid