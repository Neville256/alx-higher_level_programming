#include <Python.h>

/**
 * print_python_list_info - Python lists prints basic
 * @p: A PyObject list.
 */
void print_python_list_info(PyObject *p)
{
	int size, alloc, k;
	PyObject *obj;

	size = Py_SIZE(p);
	alloc = ((PyListObject *)p)->allocated;

	printf("[*] size of python list = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);

	for(k = 0; k < size; k++)
	{
		printf("Element %d: ", k);

		obj = PyList_GetItem(p, k);
		pintf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
