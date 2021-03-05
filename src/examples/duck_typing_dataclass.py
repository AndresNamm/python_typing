'''
Dataclasses dont have ducktyping
'''

# person_vs_comet.py
from dataclasses import dataclass

@dataclass
class Person:
  name: str
  age: int

@dataclass
class Comet:
  name: str
  age: int



def example1():
  equal = Person(name="Haley", age=42000) == Comet(name="Haley", age=42000) #
  print(equal)


def main():
  example1()


if __name__ == '__main__':
  main()


