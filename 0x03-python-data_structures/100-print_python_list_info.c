#define PY_SSIZE_T_CLEAN
#include <Python.h>

/**
 * print_python_list_info - Prints python list informations
 * @p: pointer to PyObject
 **/
void print_python_list_info(PyObject *p)
{
	int i;
	Py_ssize_t size = PyList_Size(p);
	Py_ssize_t allocsize = PyList_GET_SIZE(p);

	printf("[*] Size of the Python List = %d\n", (int)size);
	printf("[*] Allocated = %d\n", (int)allocsize);
	for (i = 0; i < size; i++)
	{
		char *type = (char *)Py_TYPE(PyList_GetItem(p, i));
		char *out;

		switch (type[0])
		{
		case 'C':
			out = "int";
			break;
		case 'J':
			out = "str";
			break;
		case '2':
			out = "float";
			break;
		case 'G':
			out = "tuple";
			break;
		case '\'':
			out = "list";
			break;
		default:
			out = type;
		}
		printf("Element %d: %s\n", i, out);
	}
}
