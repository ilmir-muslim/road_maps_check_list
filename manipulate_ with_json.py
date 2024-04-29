import json
import datetime

''' список функций: adding_current_progress, studying_stage, add_data_to_json, counting_days'''


def adding_current_progress():
    with open("members.json", "r") as file:
        members = json.load(file)

    for i in range(len(members)):
        current_progress = members[i].get('current_progress')
        if current_progress != 0:
            members[i]['studying_stage'] = studying_stage(current_progress)

    with open("members.json", "w") as file:
        json.dump(members, file, ensure_ascii=False, indent=4)


def studying_stage(studying_days):  #смотрим на каком этапе должен находиться ученик
    with open("road_map.json", "r") as file:
        road_map = json.load(file)

    for i in range(len(road_map)):
        if (studying_days in road_map[i]["дни выполнения"] or str(studying_days) == road_map[i]["дни выполнения"]) and studying_days != '0':
            stage = road_map[i].get("тема")
            return stage  #возвращает текущий этап обучения


def add_data_to_json(name, added_date):  #добавление нового участника
    with open("members.json", "r") as file:
        participants = json.load(file)
    participants.append({"name": name, "added_date": added_date})
    with open("members.json", "w") as file:
        json.dump(participants, file)


def counting_days(added_date):
    date = datetime.datetime.strptime(added_date, "%d.%m.%Y")
    return (datetime.datetime.now() - date).days
