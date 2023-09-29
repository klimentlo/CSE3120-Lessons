# CSE3120 - Object-Oriented Programming 1 - Notes

## Definitions
__Object Oriented Analysis (OOA)__ is the process of looking at a problem, system or task and identifying the tangible and intangible objects and interactions between those objects. It answers the question, _what needs to be done_.

__ Object Oriented Design (OOD) __ is the process of converting the identified process and interactions from OOA into object behaviors. It answers the question, _how things are done_.

__ Object Oriented Programming (OOP) __ is the process of implementing the outcome of object oriented design into a function program. It uses class templates to create objects that have attributes and methods.

A __Class__ is a model of an object. Classes contain _attributes_ and _behaviours_ which are inherited when objects are _instantiated_ from the class. Another definition of a class is a __blueprint__ or __template__. 
* An __Attribute__ is a property or characteristic an object possess. Each object can have different values for the attribute (An attribute is like a variable for the object). All objects instantiated from the class inherits the same attributes, which can then change with methods. 
* A __Behaviour__ is an action that can be performed on the data within an object. Behaviours are formally- named _Methods_ and are written in the same manner as a function. Therefore, methods can accept arguments into parameters that changes data within the object, and methods can return data from within the object to the rest of the program.
* Methods always have at least one parameter, ```self```, which indicates that the function is referencing the current object.
  * __Constructors__ are methods that provide the object with default attributes and creates the object from the class. In python, constructors use ``self.__init__(self)``.
  * While constructing the object like functions, they can take parameters to store data in attributes
  * In general, all attributes of the object should be present in the Constructor, even if the default value is None.

```python
from random import randint

class Die:
    '''
    A die object that can be rolled
    '''

    # Constructor 
    def __init__(self, SIDES):
        #Attributes of the object
        self.MAX_VALUE = SIDES

    # Method
    def getRoll(self):
        return randint(1, self.MAX_VALUE)

# MAIN PROGRAM CODE
DIE_1 = Die(6)
print(DIE_1.getRoll()) # print a number between 1 and 6
DIE_2 = Die(20) 
```