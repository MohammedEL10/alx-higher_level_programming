#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <stdio.h>
#include <stdlib.h>
void print_python_list_info(PyObject *p)
{
	int elem;

	printf("[*] Size of python List = %lu\n", Py_SIZE(p));
	printf("[*] Allocated = %lu\n",((PyListObject *)p)->allocated);
	for (elem = 0; elem < Py_SIZE(p); elem++)
		printf("Element %d: %s\n", elem, Py_TYPE(PyList_GetItem(p,elem))->tp_name);
}
