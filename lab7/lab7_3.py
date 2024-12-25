import json

if __name__ == "__main__":
    with open("lab7/ex_3.json") as json_file, open("lab7/ex_3_new.json", 'w') as json_new_file:
        json_dict = json.load(json_file)
        print(json_dict)
        invoice_example = json_dict['invoices'][0].copy()
        invoice_example["id"] = 3
        invoice_example["total"] = 150.0
        item_example = invoice_example["items"][0].copy()
        invoice_example["items"] = []
        item_example["name"] = "item 4"
        item_example["quantity"] = 1
        item_example["price"] = 60.0
        invoice_example["items"].append(item_example.copy())
        item_example["name"] = "item 5"
        item_example["quantity"] = 2
        item_example["price"] = 90.0
        invoice_example["items"].append(item_example)
        json_dict["invoices"].append(invoice_example)
        json.dump(json_dict, json_new_file, indent=2)