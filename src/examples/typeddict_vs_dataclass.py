'''
Unlike Typedict, dataclasses actually detect if the values passed to it mathc the type in runtime 
'''
from typing import TypedDict, Optional
import json
from dataclasses import dataclass

class PersonTD(TypedDict):
  name: str
  age: Optional[int]

@dataclass
class PersonDC():
  name: str
  age: Optional[int]



test_string = '{"randome":10}'


def example1():
  person: PersonTD = json.loads(test_string) 
  print(person) # prints out, problems not detected

def example2():
  d:dict = json.loads(test_string)
  person1: PersonDC = PersonDC(**d)
  print(person1)



def main():
  example1()
  # example2()




if __name__ == '__main__':
  main()





