import json
import datetime


def adding_current_progress():
    with open("data/members.json", "r") as file:
        members = json.load(file)

    for i in range(len(members)):
        current_progress = members[i].get('current_progress')
        if current_progress != 0:
            members[i]['studying_stage'] = studying_stage(current_progress)

    with open("data/members.json", "w") as file:
        json.dump(members, file, ensure_ascii=False, indent=4)


def studying_stage(studying_days: str):  # функция не тестилась
    with open("data/road_map.json", "r") as file:
        road_map = json.load(file)

    stage = road_map.get(studying_days)
    return stage


def add_data_to_json(name: str, added_date: str):
    with open("data/members.json", "r") as file:
        participants = json.load(file)
    participants.append({"name": name, "added_date": added_date, "current_progress": "1", "studying_stage": 'установка python и IDE, первая программа "Hello World!"'})
    with open("data/members.json", "w") as file:
        json.dump(participants, file)


def counting_days(added_date: str):
    date = datetime.datetime.strptime(added_date, "%d.%m.%Y")
    return (datetime.datetime.now() - date).days
