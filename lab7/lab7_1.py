import json
from jsonschema import validate

def validateJson(json_dict, schema_dict):
    try:
        validate(json_dict, schema_dict)
        return "ok!"
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    with open("lab7/ex_1.json") as true_json_file, open("lab7/ex_1_error.json") as error_json_file, open("lab7/ex_1_schema.json") as schema_file:
        json_dict = json.load(true_json_file)
        error_json_dict = json.load(error_json_file)
        schema_dict = json.load(schema_file)
        print(validateJson(json_dict, schema_dict))
        print(validateJson(error_json_dict, schema_dict))