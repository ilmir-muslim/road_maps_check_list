import json
from pprint import pprint


def add_data_to_json(name, added_date):  #добавление нового участника
    with open("members.json", "r") as file:
        participants = json.load(file)
    participants.append({"name": name, "added_date": added_date})
    with open("members.json", "w") as file:
        json.dump(participants, file)


#вывод словаря
with open("members.json", "r") as file:
    members = json.load(file)
    pprint(members)
