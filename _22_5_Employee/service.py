

from _22_5_Employee.dao import save_to_db

def save_data(udata):
    # business logic
    u_info = {'first_name': 'Madhu', 'last_name': 'Nettem', 'gender': 'Male', 'age': 24,
              'address': {'street_address': '1st Line', 'city': 'Bangalore', 'state': 'Karnataka',
                          'postal_code': '560066'}, 'phone_numbers': [{'type': 'home', 'number': '+91-7406900500'}]}


