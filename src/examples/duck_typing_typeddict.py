'''
TypedDicst have ducktyping
'''

# person_vs_comet.py
from typing import TypedDict

class Person(TypedDict):
  name: str
  age: int

class Comet(TypedDict):
  name: str
  age: int

def example1():
  equal = Person(name="Haley", age=42000) == Comet(name="Haley", age=42000) 
  print(equal)


def main():
  example1()


if __name__ == '__main__':
  main()
