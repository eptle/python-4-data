import json

def format_json(file_name):
    json_dict = {}
    with open(file_name, 'r') as json_read_file:
        json_dict = json.load(json_read_file)
    with open(file_name, 'w') as json_write_file:
        json.dump(json_dict, json_write_file, indent=2)
        
if __name__ == "__main__":
    format_json("lab7/ex_2.json")
    with open("lab7/ex_2.json", 'r') as json_file:
        users = json.load(json_file)
        for user in users:
            print(f'{user["name"]}: {user["phoneNumber"]}')