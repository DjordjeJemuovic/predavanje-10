import json
from methods import load_file, save_file, delete_file,clean_file

data = load_file("data/products.json")



clean_file("data/user.json")

save = save_file("data/products.json", data)

print(data)