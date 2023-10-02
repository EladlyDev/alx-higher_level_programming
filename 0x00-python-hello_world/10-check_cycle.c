#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list: the linked list to check.
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle.
 **/
int check_cycle(listint_t *list)
{
	listint_t *tmp = list;

	while (list)
	{
		if (!list->next)
			break;
		list = list->next->next;
		tmp = tmp->next;
		if (tmp == list)
			return (1);
	}

	return (0);
}
