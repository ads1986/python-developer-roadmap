# Python Developer Roadmap

When starting in a Python Development career, seems to be obvious that we need start from the language basis and fundamentals, but is not simple as that. For this reason, I started to search more for any roadmap or guideline that could be a good starting point :), so I found this two excellent articles [Python Developer Roadmap in 2021](https://dev.to/hb/python-developer-roadmap-in-2021-2bmo) and [Python Developer](https://roadmap.sh/python) that I'll use to guide my studies.

Been a experienced Java developer, I decided to share here all my learning journey with Python. I think my learning curve would be a little bit shorter thant someone starting programing now, but a think I could help who is in the same learning path.

## 1. Checklist of Learning

To have the control of what I learned and how many times I visited a specific topic, I include a number inside square brackets before the topic`s name. This number will be increased every time I revisited the topic. If the learning generate any artefact, a link will be included in the topic as in the example below :

- [1][Some Topic](https://github.com/ads1986/algorithms-and-datastructure/blob/main/src/main/java/com/algorithms/BFS.java)

## 2. Learn the basics

- [1][How Python Works](https://towardsdatascience.com/how-does-python-work-6f21fd197888)

  When we write a Python code in a file with .py extension, the compiler (example: cpython) translate this code and generate a bytecode (file with extension .pyc or .pyo) that will be interpreted by a Virtual Machine (PVM) that is also known Interpreter.

  Python is a Dynamic Typed language, so we do not define types to variables and the values  can change his type during the code execution. The the code is Interpreted (by PVM) and in runtime will report any erro related a incorret value atribution or any other problem in the code.

- [1][Python Interpreter](https://stackoverflow.com/questions/17130975/python-vs-cpython)

  The Python Language was create by [Guido Van Rossum](https://pt.wikipedia.org/wiki/Guido_van_Rossum) that implemented cpython [cpython](https://www.python.org/search/?q=cpython), write in C Language, is the original Python implementation and have all is need to run a Python app. Cpython is not  just a compiler, it has in his process a Compilation phase hat create the bytecode and an Interpreter (or PVM) that will intepretate the bytecode in a [evaluation loop](https://en.wikipedia.org/wiki/Read%E2%80%93eval%E2%80%93print_loop).

- [1][Python 2 vs Python 3](https://www.interviewbit.com/blog/difference-between-python-2-and-3/)

- [1][Running Python Code](https://www.learnpython.org/en/Hello%2C_World%21)

  a) Install Python ([click here to download](https://www.python.org/ftp/python/3.10.0/python-3.10.0-amd64.exe)) 
  
  b) Create the file script.py and insert the code :
     ```bash
        print("This line will be printed.")
     ```
  c) Run the command bellow :
     ```bash
        $ py script.py
     ```

### 2.1. Choose a Code Editor

   Because of my extensive use of [Intellij IDE](https://www.jetbrains.com/pt-br/idea/), I decided to choose the [1][PyCharm](https://www.jetbrains.com/pt-br/pycharm/), but we have so many options of Code Editors :    

  - [1][Notepad++](https://notepad-plus-plus.org)
  - [1][Vim](https://www.vim.org/)
  - [1][VSCode](https://code.visualstudio.com/docs/languages/python)
  - [1][Sublime Text](https://www.sublimetext.com/)
  - [1][Atom](https://atom.io/)
  - [1][Juypter Notebook](https://jupyter.org/)
  - [1][Google Colab](https://colab.research.google.com/?hl=pt_BR)

### 2.2. Language Basics

- [1][Variables](https://github.com/ads1986/python-developer-roadmap/blob/main/language-basics/variables.py)
- [1][Data Types and their Operations and Use](https://github.com/ads1986/python-developer-roadmap/blob/main/language-basics/datatypes.py)
- [1][Numbers, Operators, Operator Precedence](https://github.com/ads1986/python-developer-roadmap/blob/main/language-basics/numbers-operators-precedence.py)
- [1][Type Conversion](https://github.com/ads1986/python-developer-roadmap/edit/main/language-basics/type-conversion.py)
- [1][Identation](https://github.com/ads1986/python-developer-roadmap/edit/main/language-basics/identation.py)
- [1][Conditionals - If, Else, Else if, Truthy, Falsey](https://github.com/ads1986/python-developer-roadmap/blob/main/language-basics/conditionals.py)
- Loops: for, while, loop control statements (break, continue, etc)
- Functions: scope, parameters, arguments, return
- Builtin Functions
- Exceptions
- Commenting: single-line, multi-line, docstrings 

## 3. Advanced Topics

- Virtual Environments
- OOP
- Classes
- Dunder
- Methods
- Inheritance
- Decorators
- Functional Programming
- Lambda Functions
- Map, filter, zip, reduce
- Erros
- Error Handling: try, except
- File I/O
- Regex
- Import
- Debugging
- Iterators
- Await Expression

### 3.1. Modules

- Builtin
- Custom

## 4. Version Control Systems

- Basic Git Usage

## 5. Repo Hosting Services

- Github
- Gitlab
- BitBucket
- 
## 6. Package Managers

- PyPI
- Pip

## 7. Learn a Framework

### 7.1. Synchronous

- Django
- Flask
- Pyrami

### 7.2. Asynchronous

- aiohttp
- Sanic
- gevent
- Tornado

## 8. Testing your Apps

- unittest / pyUnit
- pytest
- doctest
- nose

## 9. Machine Learning/Data Science

- Tensorflow
- PyTorch
- Keras
- Scikit-learn
- Numpy
- Pandas
- ciPy
- Matplotlib
- Seaborn
- Neural Networks
- Machine Learning Algorithms
- Data
