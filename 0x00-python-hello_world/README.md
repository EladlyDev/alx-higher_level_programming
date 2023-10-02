# 0x00. Python - Hello, World
The first project on the programming language Python!

# **Learning Objectives**
At the end of this project, you are expected to be able to [explain to anyone](https://intranet.alxswe.com/rltoken/TYWTMEj3W1HhTHqMKu8kWA), **without the help of Google**:

# **General**

- **[Why Python programming is awesome](https://docs.python.org/3/tutorial/appetite.html)**
  1. Python is simple to use, but it is a real programming language, offering much more structure and support for large programs than shell scripts or batch files can offer. On the other hand, Python also offers much more error checking than C, and, being a very-high-level language, it has high-level data types built in, such as flexible arrays and dictionaries. Because of its more general data types Python is applicable to a much larger problem domain than Awk or even Perl, yet many things are at least as easy in Python as in those languages.
  2. Python allows you to split your program into modules that can be reused in other Python programs. It comes with a large collection of standard modules that you can use as the basis of your programs
  3. Python is an interpreted language, which can save you considerable time during program development because no compilation and linking is necessary.
  4. Python enables programs to be written compactly and readably. Programs written in Python are typically much shorter than equivalent C, C++, or Java programs, for several reasons:

  	 				- the high-level data types allow you to express complex operations in a single statement;
					- statement grouping is done by indentation instead of beginning and ending brackets;
					- no variable or argument declarations are necessary

  5. Python is extensible: if you know how to program in C it is easy to add a new built-in function or module to the interpreter, either to perform critical operations at maximum speed, or to link Python programs to libraries that may only be available in binary form (such as a vendor-specific graphics library). Once you are really hooked, you can link the Python interpreter into an application written in C and use it as an extension or command language for that application.
- Who created Python
  - Guido van Rossum
- [Who is Guido van Rossum](https://en.wikipedia.org/wiki/Guido_van_Rossum)
- Where does the name ‘Python’ come from
  - The BBC Tv show “[Monty Python’s Flying Circus](https://en.wikipedia.org/wiki/Monty_Python%27s_Flying_Circus)”
- [What is the Zen of Python](https://realpython.com/zen-of-python/)
- [How to use the Python interpreter](https://docs.python.org/3/tutorial/interpreter.html)
  - The interpreter operates somewhat like the Unix shell: when called with standard input connected to a tty device, it reads and executes commands interactively; when called with a file name argument or with a file as standard input, it reads and executes a script from that file.
  - A second way of starting the interpreter is python -c command [arg] ..., which executes the statement(s) in command, analogous to the shell’s -c option. Since Python statements often contain spaces or other characters that are special to the shell, it is usually advised to quote command in its entirety.
  - Some Python modules are also useful as scripts. These can be invoked using python -m module [arg] ..., which executes the source file for module as if you had spelled out its full name on the command line.
  - When a script file is used, it is sometimes useful to be able to run the script and enter interactive mode afterwards. This can be done by passing -i before the script.
  - When known to the interpreter, the script name and additional arguments thereafter are turned into a list of strings and assigned to the argv variable in the sys module. You can access this list by executing import sys. The length of the list is at least one; when no script and no arguments are given, sys.argv[0] is an empty string. When the script name is given as '-' (meaning standard input), sys.argv[0] is set to '-'. When -c command is used, sys.argv[0] is set to '-c'. When -m module is used, sys.argv[0] is set to the full name of the located module. Options found after -c command or -m module are not consumed by the Python interpreter’s option processing but left in sys.argv for the command or module to handle.
- [How to print text and variables using `print`](https://docs.python.org/3/tutorial/introduction.html#text)
- [How to use strings](https://realpython.com/python-f-strings/)
- [What are indexing and slicing in Python](https://docs.python.org/3/tutorial/introduction.html#text)
- [What is the official Python coding style and how to check your code with `pycodestyle`](https://pypi.org/project/pycodestyle/)