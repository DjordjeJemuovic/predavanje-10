import json
from methods import load_file, save_file

data = load_file("data/user.json")

data.append({"name": "Text", "price": 20000})

save_file("data/user.json", data)