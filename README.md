# **AirBnB Clone**
<p align="center">
  <img src="airbnb banner.gif" width="550" height="200">
</p>

## **📋 Table of Contents**
1. [Introduction](#introduction)
2. [Synopsis](#synopsis)
3. [Project](#Project)
  - [General Requirements](#general-requirements)
  - [Functions and system calls used](#functions-and-system-calls-used)
    - [Description of each file](#description-of-each-file)
  - [Environment](#environment)
  - [Compilation](#compilation)
  - [Testing](#testing)
    - [Interactive](#interactive-mode)
    - [Non-Interactive](#non-interactive-mode)
    - [Sample usage](#sample-usage)
    - [Stop and return to your original shell](#stop-and-return-to-your-original-shell)
  - [Project Tasks](#project-tasks)
5. [Authors](#authors)

## **📜Introduction**
* In this project we coded from scratch an AirBnb clone.
* This is the first phase of the Airbnb Clone: the console. This repository holds a command interpreter and classes (i.e. BaseModel class and several other classes that inherit from it: Amenity, City, State, Place, Review), and a command interpreter. The command interpreter, like a shell, can be activated, take in user input, and perform certain tasks to manipulate the object instances.

  [Back to Top](#project-name)
    
## **💡Synopsis**
The application begins in console.py, which calls an instance of the FileStorage class in __init__.py. This class manages all files within the storage system. For file operations, the FileStorage class calls methods from the base_model.py and file_storage.py scripts, each responsible for different aspects of the system.

[Back to Top](#project-name)
  
## **💽Project**

### **📑Python Scripts Requirements**
  - Allowed editors: `vi`, `vim`, `emacs`
  - All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
  - All your files should end with a new line
  - The first line of all your files should be exactly #!/usr/bin/python3
  - A README.md file, at the root of the folder of the project, is mandatory
  - Your code should use the pycodestyle (version 2.7.*)
  - All your files must be executable
  - The length of your files will be tested using wc
  - All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
  - All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
  - All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c       '       'print(__import__("my_module").MyClass.my_function.__doc__)')
  - A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

### **📑Python Unit Tests Requirements**
  - Allowed editors: `vi`, `vim`, `emacs`
  - All your files should end with a new line
  - All your test files should be inside a folder tests
  - You have to use the unittest module
  - All your test files should be python files (extension: .py)
  - All your test files and folders should start by test_
  - Your file organization in the tests folder should be the same as your project
  - e.g., For models/base_model.py, unit tests must be in: tests/test_models/test_base_model.py
  - e.g., For models/user.py, unit tests must be in: tests/test_models/test_user.py
  - All your tests should be executed by using this command: python3 -m unittest discover tests
  - You can also test file by file by using this command: python3 -m unittest tests/test_models/test_base_model.py
  - All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
  - All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
  - All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c   '           'print(__import__("my_module").MyClass.my_function.__doc__)')
  
### **💻Functions and system calls used**

  
#### **🗃Description of each file**

<!DOCTYPE html>
<html>

  <body>

<table style="width:100%">
  <tr>
    <th>File Name</th>
    <th>Description</th>
  </tr>
  <tr>
    <td><a href="https://github.com/semaed/holbertonschool-AirBnB_clone/blob/master/console.py">console.py</a></td>
    <td>Entry point for the application. It provides a user interface for the console. It contains the main loop that waits for input from the user, processes the input and provides output.</td>  
  </tr>
  <tr>
    <td><a href="https://github.com/semaed/holbertonschool-AirBnB_clone/blob/master/models/__init__.py">__init__.py</a></td>
    <td>Initialises a new instance of FileStorage. This is the setup file for the models package. It contains import statements for all classes in the package, creating an instance of the FileStorage class and immediately calling the reload() method on it.</td>
  </tr>
  <tr>
    <td><a href="https://github.com/jGohan-cpu/holbertonschool-simple_shell/blob/master/prompt.c">prompt.c</a></td>
    <td>Function which prints the shell prompt symbol ($)</td>
  </tr>
  <tr>
    <td><a href="https://github.com/jGohan-cpu/holbertonschool-simple_shell/blob/master/read_line.c">read_line.c</a></td>
    <td>Function that read a line of input from the user</td>
  </tr>
  <tr>
    <td><a href="https://github.com/jGohan-cpu/holbertonschool-simple_shell/blob/master/tokens.c">tokens.c</a></td>
    <td>Takes user input and splits it into and array of arguments</td>
  </tr>
  </tr>
  <tr>
    <td><a href="https://github.com/jGohan-cpu/holbertonschool-simple_shell/blob/master/env.c">env.c</a></td>
    <td>Handles the environmetal varibles</td>
  </tr>
  <tr>
    <td><a href="https://github.com/jGohan-cpu/holbertonschool-simple_shell/blob/master/shell.h">shell.h</a></td>
    <td>Header file with prototypes and header files required for the program</td>
  </tr>
  <tr>
    <td><a href="https://github.com/jGohan-cpu/holbertonschool-simple_shell/blob/master/man_1_simple_shell">man_1_simple_shell</a></td>
    <td>Simple man page of our shell</td>
  </tr>
  <tr>
    <td><a href="https://github.com/jGohan-cpu/holbertonschool-simple_shell/blob/master/AUTHORS">Authors</a></td>
    <td>Names of the authors of the project</td>
  </tr>
</table>

</body>
</html>
