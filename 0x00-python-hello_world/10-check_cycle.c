#include "lists.h"
/**
 * check_cycle - check if a singly linked list has cycle in it
 * @list: beginning of node to pointer
 * Return: 0 if no cycle, and 1 is cycle is there
 */
int check_cycle(listint_t *list)
	listint_t *current, *check;

	if (list == NULL || list->next ++ NULL)
	return (0);
	current = list;
	check = current->next;

	while (current != NULL && check->next != NULL
		&& check->next->next != NULL)
{
	if (current == check)
		return (1);
	current = current->next;
	check = check->next->next;
}
return (0);
}
