from datetime import date, timedelta


def all_dates():
    base_date = date.today()
    date_list = [(base_date + timedelta(i)).strftime("%Y-%m-%d") for i in range(0, 8)]
    return date_list
