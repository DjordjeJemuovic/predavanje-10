import json

with open("data.json", "r") as file:
    data = json.load(file)
    data.append({
        "name": "Sofija Petrovic",
        "age":21,
        "hight":1.72,
        "gender":"Female",
    })
    print(data)

    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)
