def count_studing_days(added_date):  #подчет дней обучения
    import datetime
    date = datetime.datetime.strptime(added_date, "%d.%m.%Y")
    return (datetime.datetime.now() - date).days
