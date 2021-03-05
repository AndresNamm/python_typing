'''
Pydantic basemodel based classes unlike python standard dataclassese perform runtime typecheks as well as static typecheks
'''


from pydantic.dataclasses import dataclass
from pydantic import  BaseModel
from pydantic import validator


import json


class Event(BaseModel):
    outcome: int
    probability: float
    @validator("probability")
    def probability_is_not_low(cls,v):
      if v<0.8:
        raise ValueError("Low probability")
      return v




input_string1 = '{"outcome":"sdsd","probability":"asas"}'
input_string2 = '{"outcome":"1","probability":"0.76"}'
input_string3 = '{"outcome":"1","probability":"0.8"}'


def load_and_print(input_string):
  d = json.loads(input_string)
  e = Event(**d)
  print(e.outcome)


def example1():
  load_and_print(input_string1)
def example2():
  load_and_print(input_string2)
def example3():
  load_and_print(input_string3)

def main():
  example1()
  # example2()
  # example3()



if __name__ == '__main__':
  main()

