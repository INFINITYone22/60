import json

def json_data_handling():
    # Sample JSON data
    data = {
        "name": "John Doe",
        "age": 30,
        "city": "New York"
    }

    # Write JSON data to a file
    with open("data.json", "w") as f:
        json.dump(data, f, indent=4)
    print("JSON data written to data.json")

    # Read JSON data from a file
    with open("data.json", "r") as f:
        loaded_data = json.load(f)
    print("JSON data loaded from data.json:", loaded_data)

json_data_handling()
