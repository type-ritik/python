my_dict = {
    "name": "",
    "age": None,
    "items": [],
    "tags": set(),
    "details": {},
    "cow": "Milk",
    "sheep": "Wool",
    "buffalo": "Dairy",
}


def is_empty(value):
    if value is None:
        return True
    if isinstance(value, (str, list, dict, set)) and len(value) == 0:
        return True
    return False


empty_values = []

for ky, it in my_dict.items():
    if is_empty(it):
        empty_values.append(ky)


for it in empty_values:
    del my_dict[it]

print(my_dict)
