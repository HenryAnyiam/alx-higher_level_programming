#include <Python.h>
#include <stdio.h>

/**
 * print_python_string - prints info on a python string
 * @p: python object
 */
void print_python_string(PyObject *p)
{
	wchar_t *value;
	Py_ssize_t length;

	printf("[.] string object info\n");
	if (PyUnicode_CheckExact(p))
	{
		if (PyUnicode_KIND(p) == 1)
			printf("  type: compact ascii\n");
		else
			printf("  type: compact unicode object\n");
		length = PyUnicode_GET_LENGTH(p);
		printf("  length: %li\n", length);
		value = PyUnicode_AsWideCharString(p, NULL);
		printf("  value: %ls\n", value);
		PyMem_Free(value);
	}
	else
		printf("  [ERROR] Invalid String Object\n");
}
