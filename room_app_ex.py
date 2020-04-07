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
guest_info['occupant name'] = input('Guest name? ')
guest_info['phone number'] = input('Phone number? ')


room_assign = input('Assign to which room? ')
hotel[room_assign] = guest_info
print(hotel)

#this will prompt for phone and assign to the key 'phone number for new_guest




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