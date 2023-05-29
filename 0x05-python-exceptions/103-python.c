#include <Python.h>
#include <stdio.h>
#include <stdlib.h>

void print_python_float(PyObject *p);
/**
* print_python_bytes - print python bytes info
* @p: python object
*/
void print_python_bytes(PyObject *p)
{
	Py_ssize_t length, i;
	int num = 10, c;

	fflush(stdout);
	printf("[.] bytes object info\n");
	if PyBytes_CheckExact(p)
	{
		length = PyBytes_Size(p);
		printf("  size: %li\n", length);
		printf("  trying string: ");
		for (i = 0; i < length; i++)
		{
			c = (((PyBytesObject *)(p))->ob_sval)[i];
			printf("%c", c);
		}
		printf("\n");
		if (length < 10)
			num = length + 1;
		printf("  first %i bytes:", num);
		for (i = 0; i < num; i++)
		{
			c = (((PyBytesObject *)(p))->ob_sval)[i];
			printf(" %02x", c);
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

	fflush(stdout);
	printf("[*] Python list info\n");
	if PyList_CheckExact(p)
	{
		length = PyList_GET_SIZE(p);
		alloc = ((PyListObject *)p)->allocated;
		printf("[*] Size of the Python List = %li\n", length);
		printf("[*] Allocated = %li\n", alloc);
		for (i = 0; i < length; i++)
		{
			obj = PyList_GET_ITEM(p, i);
			printf("Element %d: ", i);
			printf("%s\n", (((PyObject *)(obj))->ob_type)->tp_name);
			if (strcmp(((((PyObject *)(obj))->ob_type)->tp_name), "bytes") == 0)
				print_python_bytes(obj);
			if (strcmp(((((PyObject *)(obj))->ob_type)->tp_name), "float") == 0)
				print_python_float(obj);
		}
	}
	else
		printf("  [ERROR] Invalid List Object\n");
}

/**
 * print_python_float - print python float object info
 * @p: PyObject
 */
void print_python_float(PyObject *p)
{
	char buf[1024];
	int i;

	fflush(stdout);
	printf("[.] float object info\n");
	if PyFloat_CheckExact(p)
	{
		sprintf(buf, "%.15f", (((PyFloatObject *)(p))->ob_fval));
		printf("  value: ");
		for (i = 0; buf[i] != '.'; i++)
			printf("%c", buf[i]);
		printf("%c", buf[i]);
		i++;
		printf("%c", buf[i]);
		i++;
		while (buf[i] != '0' && buf[i] != '\0')
		{
			printf("%c", buf[i]);
			i++;
		}
		printf("\n");
	}
	else
		printf("  [ERROR] Invalid Float Object\n");
}
