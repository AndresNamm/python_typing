'''
Pydantic basemodel based objects are mutable
'''


from pydantic import BaseModel
from typing import Optional

class Tester(BaseModel):
  source: Optional[str]
  other_variable:Optional[str] 


def example1():
  exm=Tester().schema()
  print(exm)
  t1=Tester(source="a")
  print(t1)
  t1.source="k"
  print(t1)

def main():
  example1()


if __name__ == '__main__':
  main()

