from datetime import datetime 

def calculate_age_in_days_from_date_of_birth(date_of_birth:datetime)->int:
  date_now = datetime.now()
  return (date_now-date_of_birth).days

def untyped_calculate_age_in_days_from_date_of_birth(date_of_birth):
  date_now = datetime.now()
  return (date_now-date_of_birth).days

