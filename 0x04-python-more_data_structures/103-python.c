#include <Python.h>
#include <stdio.h>
#include <stdlib.h>

/**
* print_python_bytes - print python bytes info
* @p: python object
*/
void print_python_bytes(PyObject *p)
{
	Py_ssize_t length;
	int num = 10, i, hold;

	printf("[.] bytes object info\n");
	if PyBytes_CheckExact(p)
	{
		length = PyBytes_Size(p);
		printf("  size: %li\n", length);
		printf("  trying string: %s\n", PyBytes_AsString(p));
		if (length < 10)
			num = length + 1;
		printf("  first %i bytes:", num);
		for (i = 0; i < num; i++)
		{
			hold = PyBytes_AsString(p)[i];
			printf(" %02x", hold);
		}
		printf("\n");
	}
	else
		printf("  [ERROR] Invalid Bytes Object\n");
}

/**
* print_python_list - prints python list info
* @p: python object
*/
void print_python_list(PyObject *p)
{
	Py_ssize_t length;
	Py_ssize_t alloc;
	PyObject *obj;
	int i;

	if PyList_CheckExact(p)
	{
		printf("[*] Python list info\n");
		length = PyList_Size(p);
		alloc = ((PyListObject *)p)->allocated;
		printf("[*] Size of the Python List = %li\n", length);
		printf("[*] Allocated = %li\n", alloc);
		for (i = 0; i < length; i++)
		{
			obj = PyList_GET_ITEM(p, i);
			printf("Element %d: ", i);
			printf("%s\n", (((PyObject *)(obj))->ob_type)->tp_name);
		}
	}
}
