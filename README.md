# Python structure
![GitHub repo size](https://img.shields.io/github/repo-size/PitPietro/pascal-triangle)
![GitHub](https://img.shields.io/github/license/PitPietro/pascal-triangle)

It sould hae been a math library to start programming in Python and apply it to math problems, but it started testing all the stuff I was learning in Python, so it is my starting point in this language.

## Table of Contents
- [Project working](#project-working)
  - [Avoid errors](#avoid-errors)
    - [Recursive functions](#recursive-functions)
  - [Resolve problems](#resolve-problems)
    - [Import problem](#import-problem)
- [Used library](#used-modules)
  - [sys](#sys)
- [Discussion](#discussion-about-this-project)
- [Prerequisites](#prerequisites)
- [Installing](#installing)
- [Versioning](#versioning)
- [Author](#author)

## Project working

### Avoid errors

#### Recursive functions
If the the compiler (or the user) try to call self <i>recursive function</i> passing as parameter self huge number, it will
get self <code>RecursionError: maximum recursion depth exceeded in comparison</code> error because python stop calling
recursive function after 1000 calls by default. To avoid this error, let's <b>import</b> the <i>[sys](#sys)</i> module
and set <code>sys.setrecursionlimit(3000)</code> on top of the classes that implements recursive functions.<br>
A solution is given by Stack Overflow at this [link](https://stackoverflow.com/questions/20034023/maximum-recursion-depth-exceeded-in-comparison)

### Resolve problems
#### Import problem
To solve any import problem, take a look at [Real Python](https://realpython.com/absolute-vs-relative-python-imports/)
page about the topic.

## Used modules
### sys
The [sys module](https://docs.python.org/3.6/library/sys.html) (Python 3.6) provides access to some variables used or
maintained by the interpreter and to functions that interact strongly with the interpreter.

### openpyxl
Allow to work with Excel files.<br>
```bash
pip install openpyxl
```

### PyPDF2
Allow to work with PDFs. It can only extract text.
```bash
pip install pypdf2
```

### Word Documents
Allow to work with .docx files.
```bash
pip install python-docx
```

## Prerequisites
Install [PyCharm](https://www.jetbrains.com/pycharm/download/) or another Python IDE.

## Installing
Clone the repository on your computer and test yourself the library:
```bash
git clone https://github.com/PitPietro/python-structure.git
```

Move to any directory and type:
```bash
python [any-file].py
```

## Versioning
For the versions available, see the [tags on this repository](https://github.com/PitPietro/python-structure/tags).

## Author
**Pietro Poluzzi** - [PitPietro](https://github.com/PitPietro)\
See also the list of [contributors](https://github.com/PitPietro/python-structure/contributors) who participated in this project.
