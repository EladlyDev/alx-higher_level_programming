#include "lists.h"
int is_palindrome(listint_t **head)
{
	int *arr, len, i;
	listint_t *tmp = *head;

	len = linked_length(*head);
	if (len == 0)
		return (1);
	arr = malloc(sizeof(int) * len);
	for (i = 0; tmp; i++)
	{
		arr[i] = tmp->n;
		tmp = tmp->next;
	}
	for (i = 0, tmp = *head, len--; tmp; tmp = tmp->next, i++, len--)
	{
		if (tmp->n != arr[len])
		{
			free(arr);
			return (-1);
		}
	}

	free(arr);
	return (1);
}


int linked_length(listint_t *head)
{
	listint_t *tmp = head;
	int count = 0;

	if (!head)
		return (0);
	while (tmp)
	{
		count++;
		tmp = tmp->next;
	}
	return (count);
}
