#include <Python.h>
#include <stdio.h>
#include <stdlib.h>

/**
* print_python_list_info - prints information about a python list
* @p: python object
*/
void print_python_list_info(PyObject *p)
{
	Py_ssize_t length;
	Py_ssize_t alloc;
	int i;

	if PyList_CheckExact(p)
	{
		length = PyList_Size(p);
		alloc = ((PyListObject *)p)->allocated;
		printf("[*] Size of the Python List = %li\n", length);
		printf("[*] Allocated = %li\n", alloc);
		for (i = 0; i < length; i++)
		{
			printf("Element %d: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
		}
	}
}
