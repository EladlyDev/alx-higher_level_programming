#define PY_SSIZE_T_CLEAN
#include <Python.h>

void print_python_bytes(PyObject *p);

void print_python_list(PyObject *p)
{
	int i, size, allocsize;
	PyListObject *list;
	PyObject *obj;
	const char *type;

	size = ((PyVarObject *)(p))->ob_size;
	list = (PyListObject *)p;
	allocsize = list->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", allocsize);
	for (i = 0; i < size; i++)
	{
		obj = ((PyListObject *)p)->ob_item[i];
		type = (obj->ob_type)->tp_name;
		printf("Element %d: %s\n", i, type);
		if (PyBytes_Check(obj))
			print_python_bytes(obj);
	}
}

void print_python_bytes(PyObject *p)
{
	char *str;
	long int size, i, limit;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = ((PyVarObject *)p)->ob_size;
	str = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", str);

	if (size >= 10)
		limit = 10;
	else
		limit = size + 1;

	printf("  first %ld bytes:", limit);

	for (i = 0; i < limit; i++)
	{
		if (str[i] >= 0)
			printf(" %02x", str[i]);
		else
			printf(" %02x", 256 + str[i]);
	}

	printf("\n");
}
