import json
import datetime


class StudentData:
    def __init__(self, members_json: str = 'data_tests/members.json', road_map_json: str = 'data_tests/road_map.json'):
        self.members_json = members_json
        self.road_map_json = road_map_json

    def update_json(self):
        with open(self.members_json, "r") as file:
            members = json.load(file)

        for i in range(len(members)):
            members[i]['current_progress'] = self.studying_days(members[i]['added_date'])
            members[i]['studying_stage'] = self.studying_stage(members[i]['current_progress'])

        with open(self.members_json, "w") as file:
            json.dump(members, file, ensure_ascii=False, indent=4)

    def studying_stage(self, studying_days: str):
        with open(self.road_map_json, "r") as file:
            road_map = json.load(file)

        stage = road_map.get(str(studying_days))
        return stage

    def add_data_to_json(self, name: str, added_date: str):
        with open(self.members_json, "r") as file:
            participants = json.load(file)
        participants.append({"name": name, "added_date": added_date, "current_progress": "1",
                             "studying_stage": 'установка python и IDE, первая программа "Hello World!"'})
        with open(self.members_json, "w") as file:
            json.dump(participants, file)

    @staticmethod
    def studying_days(added_date: str):
        if added_date:
            date = datetime.datetime.strptime(added_date, '%d.%m.%Y')
        else:
            date = datetime.datetime.strptime('01.01.2000', '%d.%m.%Y')
        today = datetime.datetime.now()
        return (today - date).days
