#include <Python.h>

/**
 * print_python_list_info - Python list basic information printer
 * @p: A PyObject list.
 */
void print_python_list_info(PyObject *p)
{
    int size, alloc, k;
    PyObject *obj;

    size = PyList_Size(p);  // Use PyList_Size() instead of Py_SIZE() to get the size of the list
    alloc = ((PyListObject *)p)->allocated;

    printf("[*] Size of the Python list = %d\n", size);  // Updated print statement
    printf("[*] Allocated = %d\n", alloc);

    for (k = 0; k < size; k++)
    {
        printf("Element %d: ", k);

        obj = PyList_GetItem(p, k);
        printf("%s\n", Py_TYPE(obj)->tp_name);  // Corrected the typo 'pintf' to 'printf'
    }
}
