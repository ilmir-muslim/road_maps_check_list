def stading_stage(added_date):  #смотрим на каком этапе должен находиться ученик
    from count_studing_days import count_studing_days
    import json
    studing_days = count_studing_days(added_date)
    with open("road_map.json", "r") as file:
        road_map = json.load(file)
    if studing_days < 46:
        for i in range(len(road_map)):
            if str(studing_days) in road_map[i]:
                stage = road_map[i].value
