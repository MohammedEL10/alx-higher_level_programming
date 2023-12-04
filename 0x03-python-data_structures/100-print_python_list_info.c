#include <stdio.h>
#include "python.h"
/**
 * void print_python_list_info - print info about a python list
 * @p: list object
 */
void print_python_list_info(PyObject *p);
{
	int i;
	PyListObject *PP;
	/**
	 * lists in python are of the type PyListObject.Pyobjectis just a type
	 * used to pass other types around. so you need to cast your object back
	 * to its original type 
	 */
	pp = (PylistObject *)p;

	printf("[*] Size of python List = %ld\n", pp->ob_base.ob_size);
	printf("[*] Allocated = %ld\n", pp->allocated);

	for (i = 0; i < pp->ob_base.ob_size; i++)
	{
		printf("Element %d: %s\n, i, pp->ob_item[i]->ob_type->tp_name);
	}
}
