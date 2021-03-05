'''
dataclass objects dont do runtime typechecking
'''

from dataclasses import dataclass
import json

@dataclass
class Event:
    outcome: int
    probability: float


input_string1 = '{"outcome":1,"probability":0.05}'
input_string2 = '{"outcome":"sdsd","probability":"asassa"}'



def example1():
  d = json.loads(input_string1)
  e = Event(**d)
  print(e.outcome)


def example2():
  d = json.loads(input_string2)
  e = Event(**d)
  print(e.outcome)


def main():
  example1()
  example2()


  


if __name__ == '__main__':
  main()

