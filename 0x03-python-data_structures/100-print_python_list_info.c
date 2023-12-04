#include <python.h>
#include <object.h>
#include <listobject.h>

void print_python_list_info(PyObject *p);
{
	long int size = Pylist_size(p);
	int i;
	 PylistObject *obj = (PylistObject *)p;

	printf("[*] Size of python List = %li\n", size);
	printf("[*] Allocated = %li\n", obj->allocated);

	for (i = 0; i < size; i++)
	
		printf("Element %i: %s\n, i, py_type(obj->ob_item[i]->tp_name);
	
}
