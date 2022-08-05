
# Save the data into database

# Design:
'''
1. Load the data
2. Validate it
3. Implement business logic
4. Save to db accordingly

'''

from _22_5_Employee.controller import load_data
import json
if __name__ == '__main__':

    result = load_data()

