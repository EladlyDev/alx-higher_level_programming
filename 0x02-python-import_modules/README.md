# 0x02. Python - import & modules

## **Learning Objectives**

At the end of this project, you are expected to be able to [explain to anyone](https://intranet.alxswe.com/rltoken/wwTE_cGg7Ug-Vp3IQ6tmXA), **without the help of Google**:

## **General**

- Why Python programming is awesome
- [How to import functions from another file](https://docs.python.org/3/tutorial/modules.html#more-on-modules)

    There are different syntax options to accomplish this:
    - Using the `import filename` syntax, you can import the entire file and invoke its functions using the following syntax: `filename.func()`.
	- Alternatively, you can use the `from filename import func1, func2` syntax to import specific functions directly.
	- Another option is to use the `from filename import func1, func2 as newfunc1, newfunc2` syntax. This allows you to import the functions with different names.
- [How to use imported functions](https://docs.python.org/3/tutorial/modules.html#more-on-modules)

    We can invoke functions just by using their names or their imported names. If they were not imported directly and the whole module was imported, we can invoke them using the syntax: `module.funcname()`.

- [How to create a module](https://docs.python.org/3/tutorial/modules.html#modules)

    In Python, any file with a *.py extension can be treated as a module. A module is a file that contains functions, classes, or variables that can be used in other programs. By importing a module, we can access and use the functions defined in it in any other Python program.

- [How to use the built-in function `dir()`](https://docs.python.org/3/tutorial/modules.html#the-dir-function)

    The `dir(modulename)` function returns the definitions, including variables and function names, inside the module.

- [How to prevent code in your script from being executed when imported](https://docs.python.org/3/tutorial/modules.html#executing-modules-as-scripts)

    To prevent code in your script from being executed when imported, you can use the if **`name** == "**main**":` conditional statement. This statement ensures that the code block underneath it only runs if the script is being executed directly, rather than being imported as a module. By encapsulating your code within this conditional statement, you can prevent it from running when imported by another script.

- [How to use command line arguments with your Python programs](https://docs.python.org/3/tutorial/stdlib.html#command-line-arguments)

    Command line arguments are values that are passed to a Python program when it is run from the command line. They allow you to provide input or configuration options to your program. You can access command line arguments within your Python code using the `sys`module or the `argparse` module.