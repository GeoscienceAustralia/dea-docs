import datetime

def exclude_old_daily_reports(years):
    current_year = datetime.date.today().year
    previous_year = current_year - years
    return [f"validation/daily-report/{previous_year}-*"]

