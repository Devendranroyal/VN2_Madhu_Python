import json


from _22_5_Employee.service import save_data

def load_data():
    data = None
    with open('data.json') as json_file:
        data = json.load(json_file)
        print("Customer info :", data)

    # result = save_data(data)
    data = ""
    return json.dumps(data)