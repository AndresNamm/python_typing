# TYPING IN PYTHON 



By default Python does not require you to include typing in your code. However you can do this. 
For example 
~~~py
l:int=1
~~~
In here, pre runtime typechecking is performed.  This means the IDE (if your linter is setup correctly)
will throw an errr if at some point you try to do 
~~~py 
l="asoNAS"
~~~

This allows you to
  + Perform earlier error detection
  + Read the code more easily 

There is a difference between runtime and static typechecking. Static typechecking makes sure eveything is compatible within the types inside the code before its run (red lines below the code in vscode). This is not the same as checking when the code actually runs. By default Python standard libraries don't do runtime typechecking. For example you are reading in a json file and have a dataclass (ex: Event) setup with id should be of type int. Its possible for python in runtime to read in this json as Event object without throwing an error. (See example src/runtime_dataclass.py) This is due to the fact that Python by default does not do runtime typechecking. Typescript does not as well. 
To make runtime typechekcing possible we use Pydantic - see exampled src/runtime_pydantic.py


# DEPENDENCIES TO INSTALL

+ We use Pipenv to maintain the Python virtualenv and the python dependencies
  1. You need pipenv to install Python dependencies "pip install --user pipenv"
  2. You need to run setup_env.sh script. This sets up an python virtualenv based on Pipfile in the repo root directory. 
  3. VsCode should now offer to set the .venv as the default project python environment 
  4. To activate the virtualenvironment in terminal use command "pipenv shell"


# RUNNING THROUGH EXAMPLES 


Each script tries to be an example of a separete concept. The name of the script and the docstring on top of the file tries to elaborate the concept more consizely. Each function here has a main function which calls examples functions.  Run through the example function one by one by commenting out other function calls.
For example. 

~~~py
def main():
  example1()
  #example2()
~~~
then
~~~py
def main()
  #example1()
  example2()
~~~