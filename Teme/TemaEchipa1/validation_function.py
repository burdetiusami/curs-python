import datetime


def validare_data(end_date):
    try:
        # Giving the date format
        date_format = '%d/%m/%Y %H:%M'
        task_date = datetime.datetime.strptime(end_date, date_format)
        current_date = datetime.datetime.now()
        # Verify if the task_date is set in the future
        return task_date >= current_date
    except Exception:
        return False
