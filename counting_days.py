def counting_days(added_date):
    import datetime
    date = datetime.datetime.strptime(added_date, "%d.%m.%Y")
    return (datetime.datetime.now() - date).days