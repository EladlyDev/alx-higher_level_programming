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
	Py_ssize_t allocsize = ((PyListObject*)(p))->allocated;

	printf("[*] Size of the Python List = %d\n", (int)size);
	printf("[*] Allocated = %d\n", (int)allocsize);
	for (i = 0; i < size; i++)
	{
		PyObject *element = PyList_GetItem(p, i);
		const char *type = Py_TYPE(element)->tp_name;

		printf("Element %d: %s\n", i, type);
	}
}
