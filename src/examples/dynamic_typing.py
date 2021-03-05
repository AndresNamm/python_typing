'''
If setup is correct, Pylance does the check here in example 1, that the datatypes we add are wrong
'''


n:str= "1"
k:int = 1


def example1():
  s = n + k 

def example2():
  s = int(n)+k

def main():
  #example1()
  example2()


if __name__ == '__main__':
  main()
