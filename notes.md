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

An __Object__ is a unique set of data and functions instantiated from a class. An object accesses attributes and methods using _dot notation_, which identifies the object, then the attributes or method.

```
<object name>.<attribute name> --> Value
<object name>.<method name>(arguments) --> perform the method
```

Object are separate entities from each other. Once created, if one object changes attributes values, it does not change values for other objects created by the same class.

## Why OOP? (this section is important)

1. __Encapsulation__ is the process of protecting or hiding data through the implementation of an _interface_. The interface is often a collection of methods such as setter (modifier) and getter (accessor) methods that other objects can interact with. 
    * A television encapsulates all the hardware and software into a small box which the user interacts through a few buttons (remote).
    * It is important to emphasize the need for setter and getter methods and how each of the attributes within a class should only be accessed through setter and getter methods. 
    
    ```python
    class Main:
        def __init__(self):
            self.UNPROTECTED = 0
            self.__PROTECTED = 1
    
    MAIN = Main()
    print(MAIN.UNPROTECTED) # print 0
    print(MAIN.__PROTECTED) # ERROR!
    
    ```

2. __Abstraction__ is the process of setting the level of detail and complexity to what is appropriate for the given task. 
    * A driver only needs to interact with the steering, accelerator, brakes, and signals of the car to drive. But a mechanic has a much more complex understanding of the car in order to repair and maintain it. Therefore, the mechanic's abstraction of the car is more complex than the driver's. 
    * To calculate a student's average, one requires the student ID, courses taken, and grades received. While a person has many more traits (i.e. height, hair color, ethnicity, postal code, etc.), they are not needed for the purpose of the calculation and are therefore omitted.
3. __Aggregation__ is the process of grouping objects together. Objects exists independently of each other. All compositions are aggregates, but object compositions have relationships that connect objects together.
    * The students in a classroom is an aggregation of student objects.
4. __Composition__ is the process of creating a complex object by collecting several smaller objects together. 
      * A car is composed on an engine, transmission, starter, headlights, windshield, etc. Each of the car's objects are required for the car to function properly. 