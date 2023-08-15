#include <Python.h>

/**
 * print_python_list_info - Prints basic information about Python lists.
 * @p: A PythonObject list.
 */
void print_python_list_info(PyObject *p)
{
int size, alloc, i;
PyObject *obj;
size = Py_SIZE(p);
alloc = ((PyListObject *)p)->allocated;
printf("[*] Size of the Python List is equal to %d\n", size);
printf("[*] Allocated to  %d\n", alloc);
for (i = 0; i < size; i++)
{
printf("Element %d: ", i);

obj = PyList_GetItem(p, i);
printf("%s\n", Py_TYPE(obj)->tp_name);
}
}

