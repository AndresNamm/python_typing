'''
The functions are available in utils.date_utils module. Here adding a type to function parameter helps us to early detect 
potentially confusing runtime errors (like in example1()) in functions that are not explicit in the code. example2() detects error before runnning
'''

from utils.date_utils import calculate_age_in_days_from_date_of_birth, untyped_calculate_age_in_days_from_date_of_birth
from datetime import  datetime


def example1():
  age_in_days:int
  date_of_birth = "2018-01-01"
  age_in_days=untyped_calculate_age_in_days_from_date_of_birth(date_of_birth=date_of_birth) # does not check that input is datetime, only runtime error
  print(age_in_days)

def example2():
  age_in_days:int
  date_of_birth = "2018-01-01"
  age_in_days=calculate_age_in_days_from_date_of_birth(date_of_birth=date_of_birth)# checks that input is datetime
  print(age_in_days)

  

def main():
  example1()
  example2()

if __name__ == '__main__':
  main()